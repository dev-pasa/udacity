#My Favorite Apps
##Project DescriptionThis is a web application that provides a list of apps within a variety of categories and integrates google and facebook user registration and authentication. Authenticated users could have the ability to post, edit, and delete their Favorite Apps.

##Quick Start
To run this application in your local machine, you should have [vagrant](http://www.vagrantup.com/) setup. Vagrant is a tool for building and distributing development environments.

* For easy installation, you could use Udacity's [instruction](https://www.udacity.com/wiki/ud088/vagrant).
* If you already have vagrant installed. You could manually install the necessary module:
	
		pip install flask==0.9
		pip install sqlalchemy
		pip install requests
		pip install oauth2client
* I've also included two setup files `pg_config.sh` and `Vagrantfile` in the `\vagrant_setup` folder. You can copy it into the vagrant root folder before you launch vagrant.

##OAuth Login Configuration
**Google**

1. In order to connect with google, you will need to create a project at <https://console.developers.google.com/>.

	Once a project is created you need to generate OAuth ClientId in creditentials, click on `download json`to download the json file, rename it `client_secrets.json` and store it in your project folder.
2. In `/templates/login.html` paste your client id in
  `data-clientid = "Paste your google OAuth Client ID Here"`.
  
**Facebook**

1. In order to connect with google, you will need to create a project at <https://developers.facebook.com/apps>.
	
	Paste your App ID and App Secret in `fb_client_secrets.json`.

2. In `/templates/login.html` paste your App ID at `appId: 'Paste your facebook appId'`.

##To run this final project

1. Navigate to project directory inside the vagrant environment.

2. run `database_setup.py` to create the database.

3. run `data_insert.py` to populate the database.

4. run `project.py` and navigate to localhost:8000 in your browser

5. After successfully run this application, the API Endpoints can be access here:

	* JSON endpoints for Category <http://localhost:8000/category/JSON>

	* JSON endpoints for Apps <http://localhost:8000/app/JSON>