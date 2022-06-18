"""make categories table

Revision ID: 6eca51f60176
Revises: 4258e51de392
Create Date: 2022-06-15 09:57:59.591534

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6eca51f60176'
down_revision = '4258e51de392'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artikels', sa.Column('midified', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('artikels', 'modified')
    # ### end Alembic commands ###