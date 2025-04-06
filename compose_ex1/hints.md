# HINTS

## fast api server files
* **app.py** - main server script
* **requirements.txt** - python dependencies

## fast api server
* default port: 8000
* interactive api test: */docs*
* run cmd: fastapi run file.py
* **SQL_URL** env to set the database connection url, eg *user:pass@host:port*

## hint
* set restart policy for server; all container start in the same time but the database has warm up time, so maybe the app may crush few times until de sql is up