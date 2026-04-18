# App frontend (Streamlit):

# Base modules:
import sys
from pathlib import Path
import streamlit as st
import pandas as pd

# Custom modules:
from add_paths import add_paths
add_paths(["src","src/db","data"])
from c_engine import *
from c_pandas_db import *
from c_query_db import *


def main():
    st.title("Database Exploration")


if __name__ == "__main__":
    main()