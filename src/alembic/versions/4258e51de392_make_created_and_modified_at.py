"""Make_created_and_Modified_at

Revision ID: 4258e51de392
Revises: 
Create Date: 2022-06-10 13:10:59.597266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4258e51de392'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coments')
    op.drop_table('artikel_tag')
    op.drop_table('artikel_categories')
    op.drop_table('artikels')
    op.drop_table('users')
    op.drop_table('tags')
    op.drop_table('kategori')
    # ### end Alembic commands ###