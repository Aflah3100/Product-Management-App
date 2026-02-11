from database_config import db_local_session

#Return db-session object
def get_db_session():
    db_session=db_local_session()
    try:
        yield db_session
    finally:
        db_session.close()

    