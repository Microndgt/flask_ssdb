Flask-SSDB
==========

Flask-SSDB allows u to access SSDB elegantly from ur flask application.

About
------

GitHub: [https://github.com/Microndgt/flask_ssdb/](https://github.com/Microndgt/flask_ssdb/)

PyPi主页: [https://pypi.python.org/pypi/Flask-SSDB/0.0.1](https://pypi.python.org/pypi/Flask-SSDB/0.0.1)

Author主页: [http://skyrover.me](http://skyrover.me)

Installation
------

Use pip to install `Flask-SSDB`:

`pip install Flask-SSDB`


Configuration
-----

To configure access to your SSDB database server by using these settings:


- `SSDB_HOST` default is 'localhost'
- `SSDB_PORT` default is 8888
- `SSDB_PASSWORD` default is None

Usage
-----

Initialize the extension:

```
from flask_ssdb import SSDB
ssdb = SSDB()
ssdb.init_app(app)
```

Obtain a connection and set key value: ::

`ssdb.connection.set(key, value)`
