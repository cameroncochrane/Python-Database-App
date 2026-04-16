import sys
from pathlib import Path


def add_paths(paths: list[str]):
    """
    Add multiple paths to the Python system path.
    
    Inserts the given relative paths into sys.path at the beginning (index 0),
    making them the highest priority for module imports. Paths are resolved
    relative to the directory containing this file.
    
    Args:
        paths (list[str]): A list of relative path strings to add to sys.path.
                          Each path is resolved relative to the parent directory
                          of the current file.
    
    Returns:
        None
    
    Example:
        >>> add_paths(['src', 'lib', 'utils'])
        # Adds /Users/cameroncochrane/Coding Projects/Python-Database-App/src
        # Adds /Users/cameroncochrane/Coding Projects/Python-Database-App/lib
        # Adds /Users/cameroncochrane/Coding Projects/Python-Database-App/utils
    """
    project_root = Path(__file__).parent
    for path in paths:
        sys.path.insert(0, str(project_root / path))