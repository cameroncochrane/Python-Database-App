import sys
from pathlib import Path

from add_paths import add_paths
add_paths(["src","src/db","data"])

from c_engine import *
from c_pandas_db import *
from c_query_db import *

# Create an engine
engine = create_engine("sqlite:///mydata.db", True)

# Load sample data and transform to database via linking to engine
load_csv_as_db_table(data_file = "data/sales_dataset_with_customers.csv",
                     table_name = "sales", 
                     engine = engine,
                     parse_rules = {
                            "Date": "datetime",
                            "Revenue": "float",
                            "OrderID": "int",
                        })

# Query:

# Write the SQL here:
query_statement = "SELECT * FROM sales"

query_result = query_db(query_statement,engine)
print(query_result)
