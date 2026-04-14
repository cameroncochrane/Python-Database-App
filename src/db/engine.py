import sqlalchemy as sa

# Engine cocumentation: https://docs.sqlalchemy.org/en/20/tutorial/engine.html#tutorial-engine

def create_engine(location,echo):
    """
    """
    return sa.create_engine(url=location, echo=echo)
    