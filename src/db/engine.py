import os
import sqlalchemy as sa
from sqlalchemy import Engine

# Engine cocumentation: https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine

def create_engine(location: str, echo: bool) -> Engine:
    """
    Create and return a SQLAlchemy engine. If one already exists i.e. has the same
    location, that database is connected to and returned. If not, notifies the user
    and creates a new database at that location.
    """
    db_path = location.replace("sqlite:///", "")
    
    if os.path.exists(db_path):
        print(f"Connected to existing database at {db_path}")
    else:
        print(f"Database not found at {db_path}. Creating new database...")
    
    return sa.create_engine(url=location, echo=echo)



# create_engine() already connects to an existing database 
# — it doesn't drop or recreate it. The file path in location is all that matters:

# - If the .db file exists → it connects to it and uses the existing data.
# - If the .db file doesn't exist → SQLite creates a new empty one.

# Session vs Engine
####################
# Engine — the low-level connection to the database. It manages the connection pool and knows how to talk to the database 
# (dialect, credentials, file path). You typically create one per application/database.

# Session — a higher-level object that sits on top of the engine. It's the main interface for the ORM
# (Object Relational Mapper). It tracks Python objects and their state, and coordinates reading/writing them to the database.


############################################################
# At the current stage (a simple database exploration app) we don't need to worry about sessions. We can have an engine and provide SQL queries, and along with pandas
# display the query result as a dataframe.
############################################################
    