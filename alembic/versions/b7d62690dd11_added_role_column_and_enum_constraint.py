"""added role column and enum constraint

Revision ID: b7d62690dd11
Revises: bddb1af50f35
Create Date: 2023-08-17 16:05:46.437971

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from user.models.Enum.userRolesEnum import UserRolesEnum


# revision identifiers, used by Alembic.
revision: str = 'b7d62690dd11'
down_revision: Union[str, None] = 'bddb1af50f35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop the custom ENUM type if it exists
    op.execute("DROP TYPE IF EXISTS user_roles_enum")

    # Create a datatype in the database
    op.execute("CREATE TYPE user_roles_enum AS ENUM ('usr', 'adm')")

    # Create a constraint in the database that will block all values that are not part of the enum
    op.add_column('user',
                  sa.Column('role', sa.Enum(name='user_roles_enum'), server_default='usr')
                  )


def downgrade() -> None:
    # Drop the column and the constraint
    op.drop_column('user', 'role')

    # Drop the custom ENUM type
    op.execute("DROP TYPE user_roles_enum")
