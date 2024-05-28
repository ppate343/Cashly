from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from decouple import config
import os
from dotenv import load_dotenv


load_dotenv()
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')



url = URL.create(
    drivername="postgresql",
    username=db_user,
    password=db_password,
    host="localhost",
    database="whatsapp-chatbot",
    port=5432
)

engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)
    message = Column(String)
    response = Column(String)


Base.metadata.create_all(engine)

