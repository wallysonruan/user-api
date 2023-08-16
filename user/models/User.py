import sqlalchemy

from sqlalchemy.dialects.postgresql import UUID


metadata = sqlalchemy.MetaData()

table = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("id", UUID(as_uuid=True),
                      primary_key=True,
                      # The code below will call for a native function when used by the ORM to interact with PostgreSQL
                      server_default=sqlalchemy.text("gen_random_uuid()"),
                      unique=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
)
