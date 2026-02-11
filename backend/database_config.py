from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")

db_engine=create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

db_local_session=sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=db_engine
)