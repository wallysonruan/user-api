from decouple import config

"""
This module exists only to import the variables declared in the .env file into the Python context.
"""

db_type = config('DB_TYPE')
db_host = config('DB_HOST')
db_port = config('DB_PORT')
db_name = config('DB_TABLE_NAME')
db_user = config('DB_USER')
db_password = config('DB_PASSWORD')
db_url = config('DB_URL').format(
    DB_USER=db_user,
    DB_PASSWORD=db_password,
    DB_HOST=db_host,
    DB_PORT=db_port,
    DB_TABLE_NAME=db_name,
    DB_TYPE=db_type
)
