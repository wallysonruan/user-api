"""added unique constraint to user id

Revision ID: bddb1af50f35
Revises: 530aeb23b304
Create Date: 2023-08-17 15:40:32.036457

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'bddb1af50f35'
down_revision: Union[str, None] = '530aeb23b304'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('id_unique', 'user', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('id_unique', 'user', type_='unique')
    # ### end Alembic commands ###
