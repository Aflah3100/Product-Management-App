#DATABASE_URL="postgresql://postgres.jlwrkqjlmfvwmgislotw:[YOUR-PASSWORD]@aws-1-ap-southeast-2.pooler.supabase.com:6543/postgres?pgbouncer=true"
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (
    "postgresql://postgres.jlwrkqjlmfvwmgislotw:[YOUR-PASSWORD]"
    "aws-1-ap-southeast-2.pooler.supabase.com:6543/postgres?pgbouncer=true"
)


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