import pandas as pd

from sqlalchemy import Engine, text

def query_db(sql: str, engine: Engine) -> pd.DataFrame:
    """
    Execute a SQL query against a database and return results as a DataFrame.
    
    This function takes a SQL query string and a SQLAlchemy engine object,
    executes the query, and returns the results as a pandas DataFrame.
    
    Args:
        sql (str): The SQL query string to execute.
        engine (Engine): A SQLAlchemy Engine object representing the database connection.
    
    Returns:
        pd.DataFrame: A pandas DataFrame containing the query results.
    
    Raises:
        ValueError: If the query execution fails, with details about the error.
    
    Example:
        >>> from sqlalchemy import create_engine
        >>> engine = create_engine('sqlite:///database.db')
        >>> df = query_db("SELECT * FROM users WHERE age > 18", engine)
        >>> print(df.head())
    """
    try:
        return pd.read_sql(text(sql), engine)
    except Exception as e:
        raise ValueError(f"Query failed: {e}")


# Usage
# df = query_db("SELECT Region, SUM(Revenue) as TotalRevenue FROM sales GROUP BY Region", engine)
# print(df)