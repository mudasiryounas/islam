"""empty message

Revision ID: bc39d5662983
Revises: d175d2c15430
Create Date: 2020-01-09 01:47:34.124693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc39d5662983'
down_revision = 'd175d2c15430'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quran__info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('surah_number', sa.Integer(), nullable=False),
    sa.Column('surah_ar_name', sa.String(length=500), nullable=False),
    sa.Column('surah_en_name', sa.String(length=120), nullable=False),
    sa.Column('surah_en_name_translation', sa.String(length=300), nullable=False),
    sa.Column('revelation_type', sa.String(length=120), nullable=False),
    sa.Column('total_ayah', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quran_ayah_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('identifier', sa.String(length=120), nullable=False),
    sa.Column('surah_number', sa.Integer(), nullable=False),
    sa.Column('surah_ar_name', sa.String(length=500), nullable=False),
    sa.Column('surah_en_name', sa.String(length=120), nullable=False),
    sa.Column('surah_en_name_translation', sa.String(length=50000), nullable=False),
    sa.Column('revelation_type', sa.String(length=120), nullable=False),
    sa.Column('ayah_number', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('juz', sa.Integer(), nullable=False),
    sa.Column('manzil', sa.Integer(), nullable=False),
    sa.Column('page', sa.Integer(), nullable=False),
    sa.Column('ruku', sa.Integer(), nullable=False),
    sa.Column('hizb_quarter', sa.Integer(), nullable=False),
    sa.Column('sajda', sa.Boolean(), nullable=False),
    sa.Column('sajda_id', sa.Integer(), nullable=True),
    sa.Column('sajda_recommended', sa.Integer(), nullable=True),
    sa.Column('sajda_obligatory', sa.Boolean(), nullable=True),
    sa.Column('language', sa.String(length=120), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('transelator_en_name', sa.String(length=120), nullable=False),
    sa.Column('format', sa.String(length=120), nullable=False),
    sa.Column('type', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quran_ayah_info')
    op.drop_table('quran__info')
    # ### end Alembic commands ###
