Project Overview

This is a cloud-based API server build on Google App Engine to support a conference organization application that exists on the web. Using Google's Cloud Platform to build an app can effortlessly scales to support hundreds of thousands of users without worrying hardware. The Endpoints can also help to support a variety of use cases and platforms such as iOS, Android and Web.


A fully functional app is setup and can be visited at <https://coa-task-1.appspot.com>

More function are added in the back-end and you can test via this [APIs Explorer](https://apis-explorer.appspot.com/apis-explorer/?base=https://coa-task-1.appspot.com/_ah/api#p/)

Task 1: Add Sessions to a Conference

* **createSession(SessionForm, websafeConferenceKey)** ­­ open only to the organizer of the conference

	To test this function you should:
	1. Login with your google account via OAuth2.0.
	2. Create your conference on [webpage](https://coa-task-1.appspot.com/#/conference/create).
	3. Copy the websafeConferenceKey from the URL of the detail of the conference you created. e.g.
	
		<https://coa-task-1.appspot.com/#/conference/detail/agxzfmNvYS10YXNrLTFyMAsSB1Byb2ZpbGUiE25pY2t5Zm90b0BnbWFpbC5jb20MCxIKQ29uZmVyZW5jZRgBDA>
		`agxzfmNvYS10YXNrLTFyMAsSB1Byb2ZpbGUiE25pY2t5Zm90b0BnbWFpbC5jb20MCxIKQ29uZmVyZW5jZRgBDA` is the websafeConferenceKey you gonna copy.
	4. At APIs Explorer Page, choose Services > conference API v1 > [conference.createSession](https://apis-explorer.appspot.com/apis-explorer/?base=https://coa-task-1.appspot.com/_ah/api#p/conference/v1/conference.createSession) paste your websafeConferenceKey and filling the necessary information about the session you gonna add. Name and speakers are required to successfully add the session to your conference.
	
	first conference websafekey:
	agxzfmNvYS10YXNrLTFyMAsSB1Byb2ZpbGUiE25pY2t5Zm90b0BnbWFpbC5jb20MCxIKQ29uZmVyZW5jZRgBDA
	
	second conference websafekey:
	agxzfmNvYS10YXNrLTFyMQsSB1Byb2ZpbGUiE25pY2t5Zm90b0BnbWFpbC5jb20MCxIKQ29uZmVyZW5jZRiRTgw

* **getConferenceSessions(websafeConferenceKey)** ­­ Given a conference, return all sessions
* **getSessionsBySpeaker(speaker)** ­­ Given a speaker, return all sessions given by this particular speaker, across all conferences
* **getConferenceSessionsByType(websafeConferenceKey, typeOfSession)** Given a conference, return all sessions of a specified type (eg lecture, keynote, workshop)

***
App Engine application for the Udacity training course.

## Products
- [App Engine][1]

## Language
- [Python][2]

## APIs
- [Google Cloud Endpoints][3]

## Setup Instructions
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


[1]: https://developers.google.com/appengine
[2]: http://python.org
[3]: https://developers.google.com/appengine/docs/python/endpoints/
[4]: https://console.developers.google.com/
[5]: https://localhost:8080/
[6]: https://developers.google.com/appengine/docs/python/endpoints/endpoints_tool
