<p><h1>0x03. User authentication service :fire:</h1></p>

<p><h1>Description</h1></p>
In this project I began to learn/use User Authentication service<br>
In the industry, you should not implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-User](https://flask-user.readthedocs.io/en/latest/)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

## Learning Objectives
* How to declare API routes in a Flask app<br>
* How to get and set cookies<br>
* How to retrieve request form data<br>
* How to return various HTTP status codes<br>

#
## Tasks
#
## [0. User model](./user.py) <br>
In this task you will create a SQLAlchemy model named User for a database table named users (by using the mapping declaration of SQLAlchemy).
<br>
The model will have the following attributes:
<br>
* `id`, the integer primary key<br>
* `email`, a non-nullable string<br>
* `hashed_password`, a non-nullable string<br>
* `session_id`, a nullable string<br>
* `reset_token`, a nullable string<br>
```bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
from user import User

B
print(User.__tablename__)

for column in User.__table__.columns:
B
    print("{}: {}".format(column, column.type))

bob@dylan:~$ python3 main.py
users
users.id: INTEGER
users.email: VARCHAR(250)
users.hashed_password: VARCHAR(250)
users.session_id: VARCHAR(250)
users.reset_token: VARCHAR(250)
bob@dylan:~$ 
```
#
## [1. create user](./db.py)<br>
1. create user
mandatory
In this task, you will complete the DB class provided below to implement the add_user method.

```
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session
```
<br>
Note that DB._session is a private property and hence should NEVER be used from outside the DB class.
Implement the add_user method, which has two required string arguments: email and hashed_password, and returns a User object.<br>
The method should save the user to the database. No validations are required at this stage.<br>

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""

from db import DB
from user import User

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)

bob@dylan:~$ python3 main.py
1
2
bob@dylan:~$
```
#
## [2. Find user](./db.py)
#
## [3. update user](./db.py)
#
## [4. Hash password](./auth.py)
#
## [5. Register user](./auth.py)
#
## [6. Basic Flask app](./app.py)
#
## [7. Register user](./app.py)
#
## [8. Credentials validation](./auth.py)
#
## [9. Generate UUIDs](./auth.py)
#
## [10. Get session ID](./auth.py)
#
## [11. Log in](./app.py)
#
## [12. Find user by session ID](./auth.py)
#
## [13. Destroy session](./auth.py)
#
## [14. Log out](./app.py)
#
## [15. User profile](./app.py)
#
## [16. Generate reset password token](./auth.py)
#
## [17. Get reset password token](./app.py)
#
## [18. Update password](./auth.py)
#
## [Update password end-point](./app.py)
#
## [20. End-to-end integration test](./main.py)
