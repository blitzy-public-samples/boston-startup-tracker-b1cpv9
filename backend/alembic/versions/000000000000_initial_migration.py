"""Initial migration

Revision ID: 000000000000
Revises: 
Create Date: 2023-05-01 00:00:00.000000

"""
from alembic import op
from sqlalchemy import Column, Integer, String, Boolean, Float, Date, DateTime

# revision identifiers, used by Alembic.
revision = '000000000000'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create the 'users' table
    op.create_table(
        'users',
        Column('id', Integer, primary_key=True),
        Column('email', String(255), unique=True, nullable=False),
        Column('hashed_password', String(255), nullable=False),
        Column('role', String(50), nullable=False),
        Column('is_active', Boolean, default=True),
        Column('created_at', DateTime, nullable=False),
        Column('last_login', DateTime)
    )

    # Create the 'startups' table
    op.create_table(
        'startups',
        Column('id', Integer, primary_key=True),
        Column('name', String(255), nullable=False),
        Column('website', String(255)),
        Column('industry', String(100)),
        Column('sub_sector', String(100)),
        Column('employee_count', Integer),
        Column('local_employee_count', Integer),
        Column('headcount_growth', Float),
        Column('total_funding', Float),
        Column('last_funding_date', Date),
        Column('funding_stage', String(50)),
        Column('is_hiring', Boolean),
        Column('last_updated', DateTime),
        Column('created_at', DateTime, nullable=False)
    )

    # Create the 'founders' table
    op.create_table(
        'founders',
        Column('id', Integer, primary_key=True),
        Column('startup_id', Integer, nullable=False),
        Column('name', String(255), nullable=False),
        Column('title', String(100)),
        Column('linkedin_url', String(255)),
        Column('created_at', DateTime, nullable=False)
    )

    # Create the 'executives' table
    op.create_table(
        'executives',
        Column('id', Integer, primary_key=True),
        Column('startup_id', Integer, nullable=False),
        Column('name', String(255), nullable=False),
        Column('title', String(100)),
        Column('linkedin_url', String(255)),
        Column('created_at', DateTime, nullable=False)
    )

    # Create the 'investors' table
    op.create_table(
        'investors',
        Column('id', Integer, primary_key=True),
        Column('name', String(255), nullable=False),
        Column('type', String(50)),
        Column('website', String(255)),
        Column('created_at', DateTime, nullable=False)
    )

    # Create the 'funding_rounds' table
    op.create_table(
        'funding_rounds',
        Column('id', Integer, primary_key=True),
        Column('startup_id', Integer, nullable=False),
        Column('amount', Float),
        Column('date', Date),
        Column('round_type', String(50)),
        Column('created_at', DateTime, nullable=False)
    )

    # Create the 'job_postings' table
    op.create_table(
        'job_postings',
        Column('id', Integer, primary_key=True),
        Column('startup_id', Integer, nullable=False),
        Column('title', String(255), nullable=False),
        Column('department', String(100)),
        Column('description', String(1000)),
        Column('posted_date', Date),
        Column('created_at', DateTime, nullable=False)
    )

    # Create the 'news_articles' table
    op.create_table(
        'news_articles',
        Column('id', Integer, primary_key=True),
        Column('startup_id', Integer, nullable=False),
        Column('title', String(255), nullable=False),
        Column('url', String(255), nullable=False),
        Column('published_date', Date),
        Column('created_at', DateTime, nullable=False)
    )

    # Create foreign key constraints
    op.create_foreign_key('fk_founders_startup', 'founders', 'startups', ['startup_id'], ['id'])
    op.create_foreign_key('fk_executives_startup', 'executives', 'startups', ['startup_id'], ['id'])
    op.create_foreign_key('fk_funding_rounds_startup', 'funding_rounds', 'startups', ['startup_id'], ['id'])
    op.create_foreign_key('fk_job_postings_startup', 'job_postings', 'startups', ['startup_id'], ['id'])
    op.create_foreign_key('fk_news_articles_startup', 'news_articles', 'startups', ['startup_id'], ['id'])


def downgrade():
    # Drop tables in reverse order of creation
    op.drop_table('news_articles')
    op.drop_table('job_postings')
    op.drop_table('funding_rounds')
    op.drop_table('investors')
    op.drop_table('executives')
    op.drop_table('founders')
    op.drop_table('startups')
    op.drop_table('users')