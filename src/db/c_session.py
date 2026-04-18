import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

def create_session(engine):
    """
    """
    return sessionmaker(bind=engine)

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
    