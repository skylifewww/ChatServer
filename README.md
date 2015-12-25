# ChatServer
version: 1.0

Setup:
------

Inital setup
   *) git clone <path>
   *) virtualenv env
   *) source env/bin/activate
   *) pip install -r chatservice/requirements.txt


Documentation:
--------------

1. /api/v1/chats/
   *) get: Gets the latest messages which has be sent to the user
   *) post: Send message to the user
   		{"user_id":<number>, "message": "xxxxx"}
2. /api/v1/users/
   *) get: Get user details based on user id
   *) post: creates user 
        {"username": "xxxx", "email": "yyyyy@yyy.yy", "password": "zzzzz"}
   *) delete: deletes current user



Examples:
--------

API: /api/v1/chats
METHOD: GET
RESPONSE: 
	{
	  "meta": {
	    "count": 13,
	    "next": 2,
	    "current_page": "1",
	    "took": 10,
	    "previous": null
	  },
	  "messages": [
	    {
	      "sent_by": 2,
	      "message": "hai 12",
	      "sent_at": "2015-12-25T09:13:40Z",
	      "received_by": 1
	    },
	    {
	      "sent_by": 2,
	      "message": "hai 11",
	      "sent_at": "2015-12-25T09:13:34Z",
	      "received_by": 1
	    },
	    {
	      "sent_by": 2,
	      "message": "hai 10",
	      "sent_at": "2015-12-25T09:13:26Z",
	      "received_by": 1
	    },
	    {
	      "sent_by": 2,
	      "message": "hai 9",
	      "sent_at": "2015-12-25T09:13:21Z",
	      "received_by": 1
	    },
	    {
	      "sent_by": 2,
	      "message": "hai 8",
	      "sent_at": "2015-12-25T09:13:17Z",
	      "received_by": 1
	    },
	    {
	      "sent_by": 2,
	      "message": "hai 7",
	      "sent_at": "2015-12-25T09:13:10Z",
	      "received_by": 1
	    },
	    {
	      "sent_by": 2,
	      "message": "hai 6",
	      "sent_at": "2015-12-25T09:13:06Z",
	      "received_by": 1
	    },
	    {
	      "sent_by": 2,
	      "message": "hai 5",
	      "sent_at": "2015-12-25T09:13:00Z",
	      "received_by": 1
	    },
	    {
	      "sent_by": 2,
	      "message": "hai 4",
	      "sent_at": "2015-12-25T09:12:55Z",
	      "received_by": 1
	    },
	    {
	      "sent_by": 2,
	      "message": "hai 3",
	      "sent_at": "2015-12-25T09:12:50Z",
	      "received_by": 1
	    }
	  ]
	}

API: /api/v1/users/?user_id=<id>
METHOD: GET
RESPONSE: 
	{
	  "id": 2,
	  "username": "xxxx",
	  "email": "yyyyy@yyyy.yyy",
	  "date_joined": "2015-12-25T08:13:51Z",
	  "last_seen_at": "2015-12-25T08:14:40Z"
	}