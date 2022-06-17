from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI = "postgresql+psycopg2://postgres:m03kht4r1999@127.0.0.1:5432/postgres"

db = declarative_base()