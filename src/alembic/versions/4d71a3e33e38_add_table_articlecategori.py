"""add table articlecategori

Revision ID: 4d71a3e33e38
Revises: 8af4fa6df736
Create Date: 2022-06-15 13:56:37.892699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d71a3e33e38'
down_revision = '8af4fa6df736'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article_categorie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('categorie_id', sa.Integer(), nullable=True),
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['categorie_id'], ['categories.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
