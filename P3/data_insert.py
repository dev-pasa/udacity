

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Category, MyFavoriteApps, Base, User
 
engine = create_engine('sqlite:///myfavoriteappswithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()

user1 = User(name = "Huang Qiang", email = "nickyfoto@gmail.com", picture="http://avatar.chuanke.com/85/45/2382364_big_avatar.jpg")
session.add(user1)
session.commit

c1 = Category(user_id=1, name = "Business")
session.add(c1)
session.commit()

c2 = Category(user_id=1, name = "Developer Tools")
session.add(c2)
session.commit()

c3 = Category(user_id=1, name = "Education")
session.add(c3)
session.commit()

c4 = Category(user_id=1, name = "Entertainment")
session.add(c4)
session.commit()

c5 = Category(user_id=1, name = "Finance")
session.add(c5)
session.commit()

c6 = Category(user_id=1, name = "Games")
session.add(c6)
session.commit()

c7 = Category(user_id=1, name = "Graphics & Design")
session.add(c7)
session.commit()

c8 = Category(user_id=1, name = "Health & Fitness")
session.add(c8)
session.commit()

c9 = Category(user_id=1, name = "Lifestyle")
session.add(c9)
session.commit()

c10 = Category(user_id=1, name = "Medical")
session.add(c10)
session.commit()

c11 = Category(user_id=1, name = "Music")
session.add(c11)
session.commit()

c12 = Category(user_id=1, name = "News")
session.add(c12)
session.commit()

c13 = Category(user_id=1, name = "Photography")
session.add(c13)
session.commit()

c14 = Category(user_id=1, name = "Productivity")
session.add(c14)
session.commit()

c15 = Category(user_id=1, name = "Reference")
session.add(c15)
session.commit()

c16 = Category(user_id=1, name = "Social Networking")
session.add(c16)
session.commit()

c17 = Category(user_id=1, name = "Sports")
session.add(c17)
session.commit()

c18 = Category(user_id=1, name = "Travel")
session.add(c18)
session.commit()

c19 = Category(user_id=1, name = "Utility")
session.add(c19)
session.commit()

c20 = Category(user_id=1, name = "Video")
session.add(c20)
session.commit()

c21 = Category(user_id=1, name = "Weather")
session.add(c21)
session.commit()



app1 = MyFavoriteApps(user_id=1, name = "Microsoft Remote Desktop", description = "With the Microsoft Remote Desktop app, you can connect to a remote PC and your work resources from almost anywhere. Experience the power of Windows with RemoteFX in a Remote Desktop client designed to help you get your work done wherever you are.", url = "https://itunes.apple.com/us/app/microsoft-remote-desktop/id715768417?mt=12", developer = "Microsoft Corporation", os = "OS X", category_name = "Business")
session.add(app1)
session.commit()

app2 = MyFavoriteApps(user_id=1, name = "Xcode", description = "Xcode provides everything developers need to create great applications for Mac, iPhone, and iPad. Xcode brings user interface design, coding, testing, and debugging all into a unified workflow. The Xcode IDE combined with the Cocoa and Cocoa Touch frameworks, and the Swift programming language make developing apps easier and more fun than ever before.", url = "https://itunes.apple.com/us/app/xcode/id497799835?mt=12", developer = "Apple", os = "OS X", category_name = "Developer Tools")
session.add(app2)
session.commit()

print "21 categories are added!"
print "2 apps are added!"
