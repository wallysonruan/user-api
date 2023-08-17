from os import environ

from decouple import config

"""
This module exists only to import the variables declared in the .env file into the Python context.
"""

# Since both containers are on the same docker network, the application can use
# the name declared in the docker-compose.yaml as a DNS to reach the database.
# But when outside the containers, the application will use the 'localhost' to do that.
if environ.get("USER_ENV") == "PROD":
    db_host = config('DB_HOST')
else:
    db_host = config('DB_HOST_DEV')

DB_TYPE = config('DB_TYPE')
DB_PORT = config('DB_PORT')
DB_NAME = config('DB_TABLE_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_URL = config('DB_URL').format(
    DB_USER=DB_USER,
    DB_PASSWORD=DB_PASSWORD,
    DB_HOST=db_host,
    DB_PORT=DB_PORT,
    DB_TABLE_NAME=DB_NAME,
    DB_TYPE=DB_TYPE
)
