from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, MyFavoriteApps, User

from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

CLIENT_ID = json.loads(
	open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "My Favorite Apps"

engine = create_engine('sqlite:///myfavoriteappswithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create a state token to prevent request forgery.
# Store it in the session for later validation.
@app.route('/login')
def showLogin():
	state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
	login_session['state'] = state
	# RENDER THE LOGIN TEMPLATE
	return render_template('login.html', STATE = state)

@app.route('/fbconnect', methods=['POST'])
def fbconnect():
	if request.args.get('state') != login_session['state']:
		response = make_response(json.dumps('Invalid state parameter'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response
	access_token = request.data
	print "access token received %s" % access_token

	app_id = json.loads(open('fb_client_secrets.json', 'r').read())['web']['app_id']
	app_secret = json.loads(open('fb_client_secrets.json', 'r').read())['web']['app_secret']
	url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (app_id, app_secret, access_token)
	h = httplib2.Http()
	result = h.request(url, 'GET')[1]

	# Use token to get user info from API
	userinfo_url = "https://graph.facebook.com/v2.2/me"
	# strip expire tag from access token
	token = result.split("&")[0]

	url = 'https://graph.facebook.com/v2.2/me?%s' % token
	h = httplib2.Http()
	result = h.request(url, 'GET')[1]
	# print "url sent for api access:%s"%url
	# print "API JSON result: %s" % result
	data = json.loads(result)
	login_session['provider'] = 'facebook'
	login_session['username'] = data["name"]
	login_session['email'] = data["email"]
	login_session['facebook_id'] = data["id"]

	# The token must be stored in the login_session in order to properly logout, let's strip out the information before the equals sign in our token
	stored_token = token.split("=")[1]
	login_session['access_token'] = stored_token

	# Get user picture
	url = 'https://graph.facebook.com/v2.2/me/picture?%s&redirect=0&height=200&width=200' % token
	h = httplib2.Http()
	result = h.request(url, 'GET')[1]
	data = json.loads(result)

	login_session['picture'] = data["data"]["url"]

	# see if user exists
	user_id = getUserID(login_session['email'])
	if not user_id:
		user_id = createUser(login_session)
	login_session['user_id'] = user_id

	output = ''
	output += '<h1>Welcome, '
	output += login_session['username']
	output += '!</h1>'
	output += '<img src="'
	output += login_session['picture']
	output += '" style = "width: 300px; height: 300px; border-radius: 150px; -webkit-border-radius: 150px; -moz-border-radius: 150px;"> '
	flash("you are now logged in as %s" % login_session['username'])
	print "done!"
	return output

@app.route('/fbdisconnect')
def fbdisconnect():
	facebook_id = login_session['facebook_id']
	# The access token must be included to successfully logout
	# access_token = login_session['access_token']
	url = 'https://graph.facebook.com/%s/permissions' % facebook_id
	h = httplib2.Http()
	result = h.request(url, 'DELETE')[1]
	return "you have been logged out"

@app.route('/gconnect', methods=['POST'])
def gconnect():
	if request.args.get('state') != login_session['state']:
		response = make_response(json.dumps('Invalid state parameter'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response
	code = request.data
	try: 
		#Upgrade the authorization code into a credentials object
		oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
		oauth_flow.redirect_uri = 'postmessage'
		credentials = oauth_flow.step2_exchange(code)
	except FlowExchangeError:
		response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response
	# Check that the access token is valid.
	access_token = credentials.access_token
	url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
	h = httplib2.Http()
	result = json.loads(h.request(url, 'GET')[1])
	# if there was an error in the access token info, abort.
	if result.get('error') is not None:
		response = make_response(json.dumps(result.get('error')), 500)
		response.headers['Content-Type'] = 'application/json'
	# Verify that the access token is used for the intended user.
	gplus_id = credentials.id_token['sub']
	if result['user_id'] != gplus_id:
		response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
		response.headers['Content-Type'] = 'application/json'
		return response
	# Verify that the access token is valid for this app.
	if result['issued_to'] != CLIENT_ID:
		response = make_response(json.dumps("Token's user ID doesn't match app's."), 401)
		print "Token's client ID does not match app's."
		response.headers['Content-Type'] = 'application/json'
		return response
	# Check to see if user is already logged in
	stored_credentials = login_session.get('credentials')
	stored_gplus_id = login_session.get('gplus_id')
	if stored_credentials is not None and gplus_id == stored_gplus_id:
		response = make_response(json.dumps("Current user is already connected"), 200)
		response.headers['Content-Type'] = 'application/json'
		return response

	# Store the access token in the session for later use.
	login_session['credentials'] = credentials
	login_session['gplus_id'] = gplus_id

	# Get user info
	userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
	params = {'access_token': credentials.access_token, 'alt':'json'}
	answer = requests.get(userinfo_url, params=params)
	data = answer.json()

	login_session['username'] = data["name"]
	login_session['picture'] = data["picture"]
	login_session['email'] = data["email"]
	login_session['provider'] = 'google'

	# See if user exists, if it doesn't make a new one
	user_id = getUserID(login_session['email'])
	if not user_id:
		user_id = createUser(login_session)
	login_session['user_id'] = user_id

	output = ''
	output += '<h1>Welcome, '
	output += login_session['username']
	output += '!</h1>'
	output += '<img src="'
	output += login_session['picture']
	output += '" style = "width: 300px; height: 300px; border-radius: 150px; -webkit-border-radius: 150px; -moz-border-radius: 150px;"> '
	flash("you are now logged in as %s" % login_session['username'])
	print "done!"
	return output

# DISCONNECT - Revoke a current user's token and reset their login_session.
@app.route('/gdisconnect')
def gdisconnect():
	credentials = login_session.get('credentials')
	if credentials is None:
		response = make_response(json.dumps('Current user not connected.'),401)
		response.headers['Content-Type'] = 'application/json'
		return response
	# Execute HTTP GET request to revoke current token.
	access_token = credentials.access_token
	url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
	h = httplib2.Http()
	result = h.request(url, 'GET')[0]

	if result['status'] != '200':
		# For whatever reason, the given token was invalid.
		response = make_response(json.dumps("Failed to revoke token for given user.", 400))
		response.headers['Content-Type'] = 'application/json'
		return response

# JSON
@app.route('/category/JSON')
def categoryJSON():
	categories = session.query(Category).all()
	return jsonify(Category=[i.serialize for i in categories])

@app.route('/app/JSON')
def appJSON():
	apps = session.query(MyFavoriteApps).all()
	return jsonify(App=[i.serialize for i in apps])

# Frontpage
@app.route('/')
def Frontpage():
	categories = session.query(Category).all()
	apps = session.query(MyFavoriteApps).all()
	if 'username' not in login_session:
		return render_template('publicmyfavoriteapps.html', categories = categories, apps = apps)
	else:
		return render_template('myfavoriteapps.html', categories = categories, apps = apps)

# Show Each Category
@app.route('/<category_name>/')
def showCategory(category_name):
	categories = session.query(Category).all()
	category = session.query(Category).filter_by(name = category_name).first()
	apps = session.query(MyFavoriteApps).filter_by(category_name = category_name)
	count = session.query(MyFavoriteApps).filter_by(category_name = category_name).count()
	if 'username' not in login_session:
		return render_template('publiccategory.html', categories = categories, category = category, apps = apps, count = count)
	else:
		return render_template('category.html', categories = categories, category = category, apps = apps, count = count)

# Show Each App
@app.route('/<category_name>/<app_name>/')
def showApp(category_name, app_name):
	categories = session.query(Category).all()
	app = session.query(MyFavoriteApps).filter_by(name = app_name).one()
	creator = getUserInfo(app.user_id)
	if 'username' not in login_session or creator.id != login_session['user_id']:
		return render_template('publicapp.html', app = app, creator = creator, categories = categories)
	else:
		return render_template('app.html', app = app, creator = creator, categories = categories)

# Add a new app in Frontpage
@app.route('/newapp', methods = ['GET', 'POST'])
def newAppFrontPage():
	if 'username' not in login_session:
		return redirect('/login')
	if request.method == 'POST':
		newApp = MyFavoriteApps(name = request.form['name'], description = request.form['description'], url = request.form['url'], developer = request.form['developer'], os = request.form['os'], category_name= request.form['category_name'], user_id=login_session['user_id'])
		session.add(newApp)
		session.commit()
		flash("New Favorite App Added Successfully!")
		return redirect(url_for('Frontpage'))
	else:
		return render_template('newappfrontpage.html')


# Add a new app in certain category
@app.route('/<category_name>/new', methods = ['GET', 'POST'])
def newApp(category_name):
	if 'username' not in login_session:
		return redirect('/login')
	if request.method == 'POST':
		newApp = MyFavoriteApps(name = request.form['name'], description = request.form['description'], url = request.form['url'], developer = request.form['developer'], os = request.form['os'], category_name= request.form['category_name'], user_id=login_session['user_id'])
		session.add(newApp)
		session.commit()
		flash("New Favorite App Added Successfully!")
		return redirect(url_for('Frontpage'))
	else:
		return render_template('newapp.html', category_name = category_name)

# Edit App Info
@app.route('/<category_name>/<app_name>/edit', methods = ['GET', 'POST'])
def editApp(category_name, app_name):
	editApp = session.query(MyFavoriteApps).filter_by(name = app_name).one()
	if 'username' not in login_session:
		return redirect('/login')
	if editApp.user_id != login_session['user_id']:
		return "<script>function myFunction() {alert('You are not authorized to edit or delete this app info. Please add your own app in order to edit or delete.');}</script><body onload='myFunction()''>"
	if request.method == 'POST':
		if request.form['name']:
			editApp.name = request.form['name']
			editApp.description = request.form['description']
			editApp.url = request.form['url']
			editApp.developer = request.form['developer']
			editApp.os = request.form['os']
			editApp.category_name = request.form['category_name']

			session.add(editApp)
			session.commit
			flash("App Info Updated Successfully!")
			return redirect(url_for('Frontpage'))
	else:
		return render_template('editapp.html', category_name = category_name, app_name = app_name, x = editApp)

# Delete an App
@app.route('/<category_name>/<app_name>/delete', methods = ['GET', 'POST'])
def deleteApp(category_name, app_name):
	deleteApp = session.query(MyFavoriteApps).filter_by(name = app_name).one()
	if 'username' not in login_session:
		return redirect('/login')
	if deleteApp.user_id != login_session['user_id']:
		return "<script>function myFunction() {alert('You are not authorized to edit or delete this app info. Please add your own app in order to edit or delete.');}</script><body onload='myFunction()''>"
	if request.method == 'POST':
		session.delete(deleteApp)
		session.commit()
		flash("App Deleted Successfully!")
		return redirect(url_for('Frontpage'))
	else:
		return render_template('deleteapp.html', category_name = category_name, app_name = app_name, x = deleteApp)

def getUserID(email):
	try:
		user = session.query(User).filter_by(email = email).one()
		return user.id
	except:
		 return None

def getUserInfo(user_id):
	user = session.query(User).filter_by(id = user_id).one()
	return user

def createUser(login_session):
	newUser = User(name = login_session['username'], email = login_session['email'], picture = login_session['picture'])
	session.add(newUser)
	session.commit()
	user = session.query(User).filter_by(email = login_session['email']).one()
	return user.id

@app.route('/disconnect')
def disconnect():
	if 'provider' in login_session:
		if login_session['provider'] == 'google':
			gdisconnect()
			del login_session['gplus_id']
			del login_session['credentials']
		if login_session['provider'] == 'facebook':
			fbdisconnect()
			del login_session['facebook_id']
		del login_session['username']
		del login_session['email']
		del login_session['picture']
		del login_session['user_id']
		del login_session['provider']
		flash("You have successfully logged out.")
		return redirect(url_for('Frontpage'))
	else:
		flash('You were not logged in')
		return redirect(url_for('Frontpage'))

if __name__=='__main__':
	app.secret_key = "super_secret_key"
	app.debug = True
	app.run(host = '0.0.0.0', port = 8000)



