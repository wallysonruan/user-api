import databases
import env


DATABASE_URL = env.db_url
database = databases.Database(DATABASE_URL)
