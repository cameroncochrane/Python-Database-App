import sys
from pathlib import Path
import os



from src.db.engine import *
from src.db.c_pandas_db import *
from src.db.c_query_db import *

from sqlalchemy import inspect

# Create an engine

db_path = os.path.join(os.path.dirname(__file__), "databases","chinook.db")

engine = create_engine(f"sqlite:///{db_path}", False)

# Query:

# Write the SQL here:

# Return table names:
inspector = inspect(engine)
print(inspector.get_table_names())
