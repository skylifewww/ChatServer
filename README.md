# ChatServer<br/>
version: 1.0<br/>
Setup:<br/>
------<br/>
<br/>
Inital setup<br/>
   *) git clone <path><br/>
   *) virtualenv env<br/>
   *) source env/bin/activate<br/>
   *) pip install -r chatservice/requirements.txt<br/>
Documentation:<br/>
--------------<br/>
1. /api/v1/chats/<br/>
   *) get: Gets the latest messages which has be sent to the user<br/>
   *) post: Send message to the user<br/>
   		{"user_id":<number>, "message": "xxxxx"}<br/>
2. /api/v1/users/<br/>
   *) get: Get user details based on user id<br/>
   *) post: creates user <br/>
        {"username": "xxxx", "email": "yyyyy@yyy.yy", "password": "zzzzz"}<br/>
   *) delete: deletes current user<br/>
Examples:<br/>
--------<br/>
1. API: /api/v1/chats<br/>
METHOD: GET<br/>
RESPONSE: <br/>
	{<br/>
	  "meta": {<br/>
	    "count": 13,<br/>
	    "next": 2,<br/>
	    "current_page": "1",<br/>
	    "took": 10,<br/>
	    "previous": null<br/>
	  },<br/>
	  "messages": [<br/>
	    {<br/>
	      "sent_by": 2,<br/>
	      "message": "hai 12",<br/>
	      "sent_at": "2015-12-25T09:13:40Z",<br/>
	      "received_by": 1<br/>
	    },<br/>
	    {<br/>
	      "sent_by": 2,<br/>
	      "message": "hai 11",<br/>
	      "sent_at": "2015-12-25T09:13:34Z",<br/>
	      "received_by": 1<br/>
	    },<br/>
	    {<br/>
	      "sent_by": 2,<br/>
	      "message": "hai 10",<br/>
	      "sent_at": "2015-12-25T09:13:26Z",<br/>
	      "received_by": 1<br/>
	    },<br/>
	    {<br/>
	      "sent_by": 2,<br/>
	      "message": "hai 9",<br/>
	      "sent_at": "2015-12-25T09:13:21Z",<br/>
	      "received_by": 1<br/>
	    },<br/>
	    {<br/>
	      "sent_by": 2,<br/>
	      "message": "hai 8",<br/>
	      "sent_at": "2015-12-25T09:13:17Z",<br/>
	      "received_by": 1<br/>
	    },<br/>
	    {<br/>
	      "sent_by": 2,<br/>
	      "message": "hai 7",<br/>
	      "sent_at": "2015-12-25T09:13:10Z",<br/>
	      "received_by": 1<br/>
	    },<br/>
	    {<br/>
	      "sent_by": 2,<br/>
	      "message": "hai 6",<br/>
	      "sent_at": "2015-12-25T09:13:06Z",<br/>
	      "received_by": 1<br/>
	    },<br/>
	    {<br/>
	      "sent_by": 2,<br/>
	      "message": "hai 5",<br/>
	      "sent_at": "2015-12-25T09:13:00Z",<br/>
	      "received_by": 1<br/>
	    },<br/>
	    {<br/>
	      "sent_by": 2,<br/>
	      "message": "hai 4",<br/>
	      "sent_at": "2015-12-25T09:12:55Z",<br/>
	      "received_by": 1<br/>
	    },<br/>
	    {<br/>
	      "sent_by": 2,<br/>
	      "message": "hai 3",<br/>
	      "sent_at": "2015-12-25T09:12:50Z",<br/>
	      "received_by": 1<br/>
	    }<br/>
	  ]<br/>
	}<br/>
2. API: /api/v1/users/?user_id=<id><br/>
METHOD: GET<br/>
RESPONSE: <br/>
	{<br/>
	  "id": 2,<br/>
	  "username": "xxxx",<br/>
	  "email": "yyyyy@yyyy.yyy",<br/>
	  "date_joined": "2015-12-25T08:13:51Z",<br/>
	  "last_seen_at": "2015-12-25T08:14:40Z"<br/>
	}<br/>
