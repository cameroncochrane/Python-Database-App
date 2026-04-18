import sqlalchemy as sa
from sqlalchemy import Engine

# Engine cocumentation: https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine

def create_engine(location: str, echo: bool) -> Engine:
    """
    Create and return a SQLAlchemy engine. If one already exists i.e. has the same
    location, that database is connected to and returned.
    """
    return sa.create_engine(url=location, echo=echo)


# create_engine() already connects to an existing database 
# — it doesn't drop or recreate it. The file path in location is all that matters:

# - If the .db file exists → it connects to it and uses the existing data.
# - If the .db file doesn't exist → SQLite creates a new empty one.