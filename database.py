from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

# +psycopg2
engine = create_engine("postgresql://postgres:put_your_password_here@localhost:5432/Person", echo=True)

try:
    with engine.connect() as connection:
        print("Connected to PostgreSQL!")
except Exception as e:
    print("Connection failed:", e)

Base = declarative_base()

sessionLocal = sessionmaker(bind=engine)

