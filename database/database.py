import databases
import sqlalchemy

import env

"""
This module holds the objects used by the ORM to interact with the database.
"""

DATABASE_URL = env.db_url
database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata = sqlalchemy.MetaData()
metadata.create_all(engine)
