import pandas as pd

from sqlalchemy import Engine, text

def query_db(sql: str, engine: Engine) -> pd.DataFrame:
    try:
        return pd.read_sql(text(sql), engine)
    except Exception as e:
        raise ValueError(f"Query failed: {e}")


# Usage
# df = query_db("SELECT Region, SUM(Revenue) as TotalRevenue FROM sales GROUP BY Region", engine)
# print(df)