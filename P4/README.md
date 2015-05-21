##Project Overview

This is a cloud-based API server build on Google App Engine to support a conference organization application that exists on the web. Using Google's Cloud Platform to build an app can effortlessly scales to support hundreds of thousands of users without worrying hardware. The Endpoints can also help to support a variety of use cases and platforms such as iOS, Android and Web.


A fully functional app is setup and can be visited at <https://coa-task-1.appspot.com>

More function are added in the back-end and you can test via this [APIs Explorer][7]

### Products
- [App Engine][1]

### Language
- [Python][2]

### APIs
- [Google Cloud Endpoints][3]

### Setup Instructions
1. Update the value of `application` in `app.yaml` to the app ID you
   have registered in the App Engine admin console and would like to use to host
   your instance of this sample.
1. Update the values at the top of `settings.py` to
   reflect the respective client IDs you have registered in the
   [Developer Console][4].
1. Update the value of CLIENT_ID in `static/js/app.js` to the Web client ID
1. (Optional) Mark the configuration files as unchanged as follows:
   `$ git update-index --assume-unchanged app.yaml settings.py static/js/app.js`
1. Run the app with the devserver using `dev_appserver.py DIR`, and ensure it's running by visiting
   your local server's address (by default [localhost:8080][5].)
1. Generate your client library(ies) with [the endpoints tool][6].
1. Deploy your application.



###Task 1: Add Sessions to a Conference

* **createSession(SessionForm, websafeConferenceKey)** ­­ open only to the organizer of the conference

	Test method:
	1. Login with your Google account via OAuth2.0.
	2. Create your conference on [webpage](https://coa-task-1.appspot.com/#/conference/create).
	3. Copy the websafeConferenceKey from the URL of the detail of the conference you created. e.g.
	
		<https://coa-task-1.appspot.com/#/conference/detail/agxzfmNvYS10YXNrLTFyMAsSB1Byb2ZpbGUiE25pY2t5Zm90b0BnbWFpbC5jb20MCxIKQ29uZmVyZW5jZRgBDA>
		`agxzfmNvYS10YXNrLTFyMAsSB1Byb2ZpbGUiE25pY2t5Zm90b0BnbWFpbC5jb20MCxIKQ29uZmVyZW5jZRgBDA` is the websafeConferenceKey you gonna copy.
	4. At APIs Explorer Page, choose Services > conference API v1 > [conference.createSession][8] paste your websafeConferenceKey and filling the necessary information about the session you gonna add. Name and speakers are required to successfully add the session to your conference.
	
	

* **getConferenceSessions(websafeConferenceKey)**
	
	Test method: Given a conference by pasting the websafeConferenceKey to [conference.getConferenceSessions][9] return all the sessions in this conference.
	
	>For testing purpose, I put the first and second conference websafeConferenceKey here so you can easily copy and paste:

	>1st
	
	>*	
	agxzfmNvYS10YXNrLTFyMAsSB1Byb2ZpbGUiE25pY2t5Zm90b0BnbWFpbC5jb20MCxIKQ29uZmVyZW5jZRgBDA
	
	>2ed
	
	>* agxzfmNvYS10YXNrLTFyMQsSB1Byb2ZpbGUiE25pY2t5Zm90b0BnbWFpbC5jb20MCxIKQ29uZmVyZW5jZRiRTgw
* **getSessionsBySpeaker(speaker)** 

	Test method: Given a speaker by pasting the speaker's name to [conference.getConferenceSessionsBySpeaker][10] to get all sessions given by this speaker, across all conferences.

* **getConferenceSessionsByType(websafeConferenceKey, typeOfSession)** 
	
	Test method: Given a conference by pasting the websafeConferenceKey and the type of session you search for at [conference.getConferenceSessionsByType][11] return all sessions of a specified type (eg lecture, keynote, workshop)

###Task 2: Add Sessions to User Wishlist

* **addSessionToWishlist(SessionKey)**
	
	Test method: 
	
	1. Use **getConferenceSessions(websafeConferenceKey)** API to return a list of sessions in a particular conference and copy the SessionKey of a session you want to add to your wishlist.
	
	2. Paste the SessionKey to [conference.addSessionToWishlist][12] to add the session to your wishlist.
	
* **getSessionsInWishlist()**
	
	Test method: visit [conference.getSessionsInWishlist][13], login with your Google account to get all the sessions you've added to your wishlist.

###Task 3: Work on indexes and queries

* **conference.avoidSessionsByTypeAndTime(startTime, typeOfSession)**

	Test method:
	1. Input the latest time you could make to attend the session using 24 hour notation (saying if 7pm is 19 in this case).
	2. Input the name of type you are NOT interested in, in order to return all other types of session with start time earlier than you expected.

* **conference.conferenceSeatsAvailableByCityDESC**

	Purpose: this query could help you easily know which conference in this city has the most seats available as well as the least seats available.
	
	Test method: visit [conference.conferenceSeatsAvailableByCityDESC][15], input the city name, you got all the conferences in this city by order of their seats available in a descending order.

* **conference.countSessionsByConference**

	Purpose: this query could help you easily know how many sessions in a particular conference.
	
	Test method: visit [conference.countSessionsByConference][16], paste the websafeConferenceKey as input, you get the number of sessions in this particular conference.
	
###Task 4: Memcache Entry

* **getFeaturedSpeaker()**

	Test method: visit [conference.getFeaturedSpeaker][14] then Execute to see the result.
	



[1]: https://developers.google.com/appengine
[2]: http://python.org
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://console.developers.google.com/
[5]: https://localhost:8080/
[6]: https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool
[7]: https://apis-explorer.appspot.com/apis-explorer/?base=https://coa-task-1.appspot.com/_ah/api#p/
[8]: https://apis-explorer.appspot.com/apis-explorer/?base=https://coa-task-1.appspot.com/_ah/api#p/conference/v1/conference.createSession
[9]: https://apis-explorer.appspot.com/apis-explorer/?base=https://coa-task-1.appspot.com/_ah/api#p/conference/v1/conference.getConferenceSessions
[10]: https://apis-explorer.appspot.com/apis-explorer/?base=https://coa-task-1.appspot.com/_ah/api#p/conference/v1/conference.getConferenceSessionsBySpeaker
[11]: https://apis-explorer.appspot.com/apis-explorer/?base=https://coa-task-1.appspot.com/_ah/api#p/conference/v1/conference.getConferenceSessionsByType
[12]: https://apis-explorer.appspot.com/apis-explorer/?base=https://coa-task-1.appspot.com/_ah/api#p/conference/v1/conference.addSessionToWishlist
[13]: https://apis-explorer.appspot.com/apis-explorer/?base=https://coa-task-1.appspot.com/_ah/api#p/conference/v1/conference.getSessionsInWishlist
[14]: https://apis-explorer.appspot.com/apis-explorer/?base=https://coa-task-1.appspot.com/_ah/api#p/conference/v1/conference.getFeaturedSpeaker
[15]: https://apis-explorer.appspot.com/apis-explorer/?base=https://coa-task-1.appspot.com/_ah/api#p/conference/v1/conference.conferenceSeatsAvailableByCityDESC
[16]: https://apis-explorer.appspot.com/apis-explorer/?base=https://coa-task-1.appspot.com/_ah/api#p/conference/v1/conference.countSessionsByConference
