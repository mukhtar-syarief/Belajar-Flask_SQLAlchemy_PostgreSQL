"""make categories table

Revision ID: a669a2edf309
Revises: 6eca51f60176
Create Date: 2022-06-15 10:46:12.660671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a669a2edf309'
down_revision = '6eca51f60176'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    # ### end Alembic commands ###
