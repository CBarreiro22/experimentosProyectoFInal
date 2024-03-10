import os
import uuid
from datetime import datetime

from dotenv import load_dotenv
from sqlalchemy import Column, DateTime, create_engine, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import UUIDType
from sqlalchemy import inspect

ENV = None

try:
    ENV = os.getenv('ENV')

except KeyError:
    print("no testing mode")

if not ENV is None and ENV == 'test':

    engine = create_engine('sqlite:///:memory:')
    # Load environment variables from the .env.development file
else:
    loaded = load_dotenv('.env.development')
    # Create a SQLAlchemy engine using environment variables for database connection
    print(os.getenv("DB_USER"))
    engine = create_engine(
        f'postgresql://{os.environ["DB_USER"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/{os.environ["DB_NAME"]}',pool_size=20)
    # engine = create_engine(
    #     f'postgresql://postgres:postgres@localhost:5432/mydatabase',pool_size=20)

# Create a scoped database session
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Create a base class for declarative models
Base = declarative_base()
Base.query = db_session.query_property()


# Initialize the database schema
def init_db():
    inspector = inspect(engine)
    if not inspector.has_table("athlete"):
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        print("La base de datos y la tabla han sido creadas.")
    else:
        print("La tabla athlete ya existe en la base de datos.")


# Define a base class for models with common attributes

class Model(Base):
    __abstract__ = True

    # Common attributes for all models
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow)

    def __init__(self):
        # Set the creation and update timestamps
        self.createdAt = datetime.utcnow()
        self.updatedAt = datetime.utcnow()