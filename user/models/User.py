import sqlalchemy
from sqlalchemy import UniqueConstraint, CheckConstraint

from sqlalchemy.dialects.postgresql import UUID


metadata = sqlalchemy.MetaData()

table = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("id", UUID(as_uuid=True),
                      primary_key=True,
                      # The code below will call for a native function when used by the ORM to interact with PostgreSQL
                      server_default=sqlalchemy.text("gen_random_uuid()")),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),

    # This strategy allows to set a name to the constraint
    UniqueConstraint("id", name="id_unique"),
)
