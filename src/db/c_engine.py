import sqlalchemy as sa
from sqlalchemy import Engine

# Engine cocumentation: https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine

def create_engine(location: str, echo: bool) -> Engine:
    """
    Create and return a SQLAlchemy engine.
    """
    return sa.create_engine(url=location, echo=echo)
    