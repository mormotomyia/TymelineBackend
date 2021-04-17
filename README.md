# Backend Implementation fpr custom-tymeline frontend


## Motivation

demonstrate ability to design and build complex interfaces and realize them as REST-APIs

Experiment with how do design Interfaces

Document process of creating interfaces (not the backend implementation to support them!)


1. Define response payload
2. Define response scope
3. Define response exceptions
4. Write Tests for all in 3.
5. Write code to pass all tests



## Implementation

Interface 

```json
 [
    { 
    id: number | string,
    length: number,
    content:{text:string},
    start:number, #unixTimestamp in seconds
    canChangeLength:boolean,
    canMove:boolean
    },
    ]
```

2. 
GET /{id} -> {id:{id}} -> 200
GET /{id} -> null -> 204

GET /all -> [{},..] ->200/206
*think about returning index to fetch further data*

POST /create -> {id} -> 201
POST /create -> null -> 400 # on invalid payload
POST /create -> null -> 403 # on invalid auth
POST /create -> null -> 500 # on any backend error

payload : interface

POST /update/{id} -> id -> 200
POST /update/{id} -> id -> 400 # on invalid payload
POST /update/{id} -> id -> 403 # on invalid auth
POST /update/{id} -> null -> 500 # on any backend error

payload : interface

DELETE /delete/{id} -> id -> 200
DELETE /delete/{id} -> id -> 200 # on invalid payload! deleting a not existing id will always succeed! 
DELETE /delete/{id} -> id -> 403 # on invalid auth
DELETE /delete/{id} -> null -> # on any backend error

payload : none



