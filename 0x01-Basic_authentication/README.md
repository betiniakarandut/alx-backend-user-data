<p><h1>0x01. Basic authentication :fire:</h1></p>

<p><h2>Description :house:</h2></p>
In this project I began to practice Basic Authentication.<br>
The HTTP Authorization request header can be used to provide credentials that authenticate a user agent with a server, allowing access to a protected resource.
<br>
The Authorization header is usually, but not always, sent after the user agent first attempts to request a protected resource without credentials. The server responds with a 401 Unauthorized message that includes at least one WWW-Authenticate header. This header indicates what authentication schemes can be used to access the resource (and any additional information needed by the client to use them). The user-agent should select the most secure authentication scheme that it supports from those offered, prompt the user for their credentials, and then re-request the resource (including the encoded credentials in the Authorization header).

## Learning Objectives

- What authentication means<br>
- What Base64 is<br>
- How to encode a string in Base64<br>
- What Basic authentication means<br>
- How to send the Authorization header<br>

<p><h2>Tasks :pencil:</h2></p>

## [0. Simple-basic-API](./0x01-Basic_authentication)<br>

Download and start your project from this archive.zip

In this archive, you will find a simple API with one model: User. Storage of these users is done via a serialization/deserialization in files.

**Setup and start server**

```bob@dylan:~$ pip3 install -r requirements.txt
...
bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Serving Flask app "app" (lazy loading)
...
bob@dylan:~$
```

Use the API (in another tab or in your browser)

```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/status HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 16
< Access-Control-Allow-Origin: *
< Server: Werkzeug/1.0.1 Python/3.7.5
< Date: Mon, 18 May 2020 20:29:21 GMT
<
{"status":"OK"}
* Closing connection 0
bob@dylan:~$
```

#

## [1. Error handler: Unauthorized](./api/v1/app.py)<br>

What the HTTP status code for a request unauthorized? 401 of course!

Edit `api/v1/app.py`:

Add a new error handler for this status code, the response must be:
a JSON: `{"error": "Unauthorized"}`
status code `401`
you must use `jsonify` from `Flask`
For testing this new error handler, add a new endpoint in `api/v1/views/index.py`:

Route: `GET /api/v1/unauthorized`
This endpoint must raise a `401` error by using abort - Custom Error Pages
By calling `abort(401)`, the error handler for `401 `will be executed.

In the first terminal:

```bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

<br>
In a second terminal:

```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/unauthorized"
{
  "error": "Unauthorized"
}
bob@dylan:~$

bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/unauthorized" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/unauthorized HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 401 UNAUTHORIZED
< Content-Type: application/json
< Content-Length: 30
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 24 Sep 2017 22:50:40 GMT
<
{
  "error": "Unauthorized"
}
* Closing connection 0
bob@dylan:~$
```

#

## [2. Error handler: Forbidden](./api/v1/app.py) <br>

What the `HTTP status code` for a request where the user is authenticate but not allowed to access to a resource? `403` of course!

Edit `api/v1/app.py`:

Add a new error handler for this status code, the response must be:
a JSON: `{"error": "Forbidden"}`
status code `403`
you must use `jsonify` from `Flask`
For testing this new error handler, add a new endpoint in `api/v1/views/index.py`:

Route: `GET /api/v1/forbidden`
This endpoint must raise a 403 error by using abort - Custom Error Pages
By calling `abort(403)`, the error handler for `403` will be executed.

In the first terminal:

```
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In a second terminal:

```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/forbidden"
{
  "error": "Forbidden"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/forbidden" -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/forbidden HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 403 FORBIDDEN
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 24 Sep 2017 22:54:22 GMT
<
{
  "error": "Forbidden"
}
* Closing connection 0
bob@dylan:~$
```

#

## [3. Auth class](./api/v1/auth) <br>

Now you will create a class to manage the API authentication.
<br>

- Create a folder `api/v1/auth`<br>
- Create an empty file `api/v1/auth/__init__.py`<br>
- Create the `class Auth`:<br>
  - in the file `api/v1/auth/auth.py`<br>
  - `import request from flask`<br>
  - `class name Auth`<br>
  - public method `def require_auth(self, path: str, excluded_paths: List[str]) -> bool:` that `returns False` - path and excluded_paths will be used later, now, you don’t need to take care of them<br>
  - public method `def authorization_header(self, request=None) -> str:` that returns None - request will be the `Flask` request object<br>
  - public method `def current_user(self, request=None) -> TypeVar('User'):` that `returns None` - request will be the `Flask` request object<br>

This class is the template for all authentication system you will implement.

```
bob@dylan:~$ cat main_0.py
#!/usr/bin/env python3
""" Main 0
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(a.authorization_header())
print(a.current_user())

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_0.py
False
None
None
bob@dylan:~$
```

#

## [4. Define which routes don't need authentication](./api/v1/auth/auth.py) <br>

Update the method `def require_auth(self, path: str, excluded_paths: List[str]) -> bool:` in Auth that returns `True` if the path is not in the list of strings excluded_paths:<br>

Returns `True` if path is `None`<br>
Returns `True` if excluded_paths is `None` or `empty`<br>
Returns `False` if path is in excluded_paths<br>
You can assume excluded_paths contains string path always ending by a `/`<br>
This method must be slash tolerant: path=`/api/v1/`status and path=`/api/v1/status/` must be returned `False` if excluded_paths contains `/api/v1/status/`

```
bob@dylan:~$ cat main_1.py
#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth(None, None))
print(a.require_auth(None, []))
print(a.require_auth("/api/v1/status/", []))
print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))

bob@dylan:~$
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_1.py
True
True
True
False
False
True
True
bob@dylan:~$
```

#

## [5. Request validation!](./api/v1/app.py) <br>

Now you will validate all requests to secure the API:
<br>

Update the method `def authorization_header(self, request=None) -> str:` in `api/v1/auth/auth.py`:

- If request is `None`, returns `None`<br>
- If request doesn’t contain the header key Authorization, returns `None` <br>
- Otherwise, return the value of the header request `Authorization` <br>

Update the file `api/v1/app.py`:

- Create a variable `auth` initialized to `None` after the `CORS` definition <br>
- Based on the environment variable `AUTH_TYPE`, load and assign the right instance of authentication to `auth` <br>
- if `auth:`
  - import `Auth` from `api.v1.auth.auth` <br>
  - create an instance of Auth and assign it to the variable `auth` <br>

Now the biggest piece is the filtering of each request. For that you will use the Flask method `before_request`

- Add a method in `api/v1/app.py` to handler before_request
  _ if `auth` is `None`, do nothing <br>
  _ if `request.path` is not part of this list [`'/api/v1/status/'`, `'/api/v1/unauthorized/'`, `'/api/v1/forbidden/'`], do nothing - you must use the method require_auth from the auth instance <br>
  _ if `auth.authorization_header(request)` returns `None`, raise the error 401 - you must use `abort` <br>
  _ if `auth.current_user(request)` returns `None`, `raise` the error `403` - you must use `abort`<br>
  In the first terminal:

```
bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=auth python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

In a second terminal:

```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status/"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{
  "error": "Forbidden"
}
bob@dylan:~$
```

#

## Author

[Betini Akarandut](https://www.github.com/betiniakarandut) :fire:
