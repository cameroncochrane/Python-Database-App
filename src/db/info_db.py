import os
from sqlalchemy import Engine, inspect



def get_db_info(engine: Engine) -> dict:
    """
    Extract descriptive information about a database from a SQLAlchemy engine.

    Args:
        engine (Engine): SQLAlchemy Engine instance for the database connection.

    Returns:
        dict: A dictionary with the following keys:
            - dialect (str): The database dialect/driver, e.g. "sqlite", "postgresql".
            - database (str): Database name, or file path for file-based databases.
            - host (str | None): Hostname, or None for file-based databases.
            - port (int | None): Port number, or None for file-based databases.
            - username (str | None): Connected username, if applicable.
            - is_local (bool): True if the connection is local (SQLite, or host is
              localhost/127.0.0.1), False otherwise.
            - schema_names (list[str]): Available schema names.
            - default_schema (str | None): The default schema name.
            - table_names (list[str]): Names of all tables in the default schema.
            - view_names (list[str]): Names of all views in the default schema.
            - size_bytes (int | None): File size in bytes, if file-based and the
              file exists on disk. None otherwise.
            - size_human (str | None): Human-readable file size (e.g. "12.4 KB"),
              or None if not applicable.

    Example:
        >>> engine = create_engine("sqlite:///database.db", False)
        >>> info = get_db_info(engine)
        >>> print(info["table_names"])
    """
    url = engine.url
    inspector = inspect(engine)

    dialect = url.drivername
    is_sqlite = dialect.startswith("sqlite")

    # Local vs remote: SQLite is always local (file on disk); otherwise check host
    is_local = is_sqlite or url.host in (None, "localhost", "127.0.0.1")

    # File size only applies to file-based databases like SQLite
    size_bytes = None
    size_human = None
    if is_sqlite and url.database and os.path.exists(url.database):
        size_bytes = os.path.getsize(url.database)
        size_human = _human_readable_size(size_bytes)

    return {
        "dialect": dialect,
        "database": url.database,
        "host": url.host,
        "port": url.port,
        "username": url.username,
        "is_local": is_local,
        "schema_names": inspector.get_schema_names(),
        "default_schema": inspector.default_schema_name,
        "table_names": inspector.get_table_names(),
        "view_names": inspector.get_view_names(),
        "size_bytes": size_bytes,
        "size_human": size_human,
    }


def _human_readable_size(num_bytes: int) -> str:
    """Convert a byte count into a human-readable string (e.g. '12.4 KB')."""
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} PB"


# Usage
# from db.engine import create_engine
# engine = create_engine("sqlite:///databases/chinook.db", False)
# info = get_db_info(engine)
# print(info)