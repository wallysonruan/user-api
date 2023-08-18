import sqlalchemy
from sqlalchemy import UniqueConstraint

from sqlalchemy.dialects.postgresql import UUID

from user.models.enums.userRolesEnum import UserRolesEnum

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

    # A custom function was created in the alembic file responsible for migrating this code
    # b7d62690dd11_added_role_column_and_enum_constraint
    sqlalchemy.Column("role",
                      sqlalchemy.Enum(
                          UserRolesEnum, name="user_roles_enum", create_type=False)
                      ),

    # This strategy allows to set a name to the constraint
    UniqueConstraint("id", name="id_unique"),
)
