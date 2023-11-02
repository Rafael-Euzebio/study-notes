# HTTP Request Methods
HTTP Request Methods are messages sent from a client to a server that indicates the intention of performing an action, like requesting a web page or inserting values in a database


## Example
This is a `GET` request to get the main page from `www.example.com`
```http
GET / HTTP/1.1
Host: example.com
User-Agent: curl/7.81.0
Accept: */*
```

A request method always generate a [[CS50x HTTP Response]] from the server

| Request | Description |
|-------- | ----------- |
| GET     | Get content from the server (A web page, info about a user, etc)
| POST    | Send information to the server (insert values into a database)
| PUT     | Replace information on the server (change existing values for an user in a database)
| DELETE  | Delete information on the server (Delete a user from a database)

```mermaid
flowchart LR
device--- GET['GET /'] --> Server
```
