import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

def create_session(engine):
    """
    """
    return sessionmaker(bind=engine)

    