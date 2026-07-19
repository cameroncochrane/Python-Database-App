# App frontend (Streamlit):

# Base modules:
import sys
import os
from pathlib import Path
import streamlit as st
import pandas as pd
from sqlalchemy import inspect

from src.db.engine import create_engine
from src.db.pandas_db import query_to_df


def main():

    # Initialise necessary session_state variables:

    # Dataframe to display
    if "df" not in st.session_state:
        st.session_state.df = None
    # Location address of the database:
    if "db_loc" not in st.session_state:
        st.session_state.db_loc = None
    # Engine:
    if "engine" not in st.session_state:
        st.session_state.engine = None
    # List of db tables:
    if "tables_list" not in st.session_state:
        st.session_state.tables_list = None


    # App layout
    st.title("Database Exploration")

    # Check for .db files in databases directory
    databases_dir = Path("databases")
    db_files = []
    if databases_dir.exists():
        db_files = list(databases_dir.glob("*.db"))
    
    # Connect to database at a specified location
    if db_files:
        selected_db = st.selectbox("Select a database file", db_files)
        st.session_state.db_loc = f"sqlite:///{selected_db}"
    else:
        st.session_state.db_loc = st.text_input("Database Location", placeholder="Enter the path to your database")

    if st.button("Connect"):
        try:
            if st.session_state.db_loc is not None:
                db_location = st.session_state.db_loc

                engine = create_engine(location=db_location, echo=False)

                st.session_state.engine = engine

        except Exception as e:
            st.error(f"Failed to connect to database: {str(e)}")
    

    # Return the list of database tables
    if st.session_state.engine is not None:
        inspector = inspect(st.session_state.engine)
        tables_list = inspector.get_table_names() # Inspector method is more widespread among different db types.
        st.session_state.tables_list = tables_list
        
        if st.session_state.tables_list:
            st.subheader("Available Tables")
            st.write(st.session_state.tables_list)
        elif not st.session_state.tables_list:
            st.write("No tables found")
    
    
if __name__ == "__main__":
    main()