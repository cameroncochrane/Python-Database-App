import pandas as pd

import sqlalchemy as sa
from sqlalchemy import Engine, Integer, Float, Text, text
from sqlalchemy.types import DateTime


def load_csv_to_db(data_file: str, table_name: str, engine: Engine, parse_rules: dict = None):
    """
    Load a CSV file into a database table with optional type parsing.

    This function reads a CSV file using pandas, applies optional type conversions
    based on provided parsing rules, and writes the data to a SQL database table
    using SQLAlchemy.

    Args:
        data_file (str): Path to the CSV file to load.
        table_name (str): Name of the table to create or replace in the database.
        engine (Engine): SQLAlchemy Engine instance for database connection.
        parse_rules (dict, optional): Dictionary mapping column names to data types.
            Supported dtype values: "datetime", "float", "int", or any valid pandas dtype.
            Defaults to None (no type conversion applied).

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified CSV file does not exist.
        pd.errors.ParserError: If the CSV file cannot be parsed correctly.
        PermissionError: If there are insufficient permissions to access the file.
        ValueError: If a column cannot be converted to the specified datatype.

    Examples:
        >>> engine = create_engine("sqlite:///database.db")
        >>> parse_rules = {"date_column": "datetime", "amount": "float"}
        >>> load_csv_to_db("data.csv", "my_table", engine, parse_rules)
    """
    try:
        data_df = pd.read_csv(data_file)
        sql_dtype_map = {}

        if parse_rules:
            for column, dtype in parse_rules.items():
                if column not in data_df.columns:
                    continue

                if dtype == "datetime":
                    data_df[column] = pd.to_datetime(data_df[column])
                    sql_dtype_map[column] = DateTime()
                elif dtype == "float":
                    data_df[column] = pd.to_numeric(data_df[column])
                    sql_dtype_map[column] = Float()
                elif dtype == "int":
                    data_df[column] = pd.to_numeric(data_df[column], downcast="integer")
                    sql_dtype_map[column] = Integer()
                else:
                    data_df[column] = data_df[column].astype(dtype)

        data_df.to_sql(table_name, engine, if_exists="replace", index=False, dtype=sql_dtype_map or None)
        print(len(data_df))

    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {data_file}")
    except pd.errors.ParserError as e:
        raise pd.errors.ParserError(f"Failed to parse CSV file: {e}")
    except PermissionError:
        raise PermissionError(f"Permission denied accessing file: {data_file}")
    except ValueError as e:
        raise ValueError(f"Failed to convert column datatype: {e}")

def query_to_df(sql: str, engine: Engine) -> pd.DataFrame:
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
        >>> df = query_to_df("SELECT * FROM users WHERE age > 18", engine)
        >>> print(df.head())
    """
    try:
        return pd.read_sql(text(sql), engine)
    except Exception as e:
        raise ValueError(f"Query failed: {e}")