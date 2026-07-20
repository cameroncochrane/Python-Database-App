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
from src.db.info_db import get_db_info


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
    # db basic information (from engine.inspect)
    if "db_info" not in st.session_state:
        st.session_state.db_info = None


    # App layout
    st.title("Database Viewer")

    # Check for .db files in databases directory
    databases_dir = Path("databases")
    db_files = []
    if databases_dir.exists():
        db_files = list(databases_dir.glob("*.db"))
    
    # Connect to database in the databases directory:
    if db_files:
        selected_db = st.selectbox("Select a database file", db_files)
        st.session_state.db_loc = f"sqlite:///{selected_db}"
    if st.button(label="Connect",key="dir_db_connect"):
        try:
            if st.session_state.db_loc is not None:
                db_location = st.session_state.db_loc

                engine = create_engine(location=db_location, echo=False)

                st.session_state.engine = engine

        except Exception as e:
            st.error(f"Failed to connect to the database in the local directory: {str(e)}")
    
    # Connect to a database via a URL:
    url_db = st.text_input("Database Location", placeholder="Enter the URL to your database")
    if url_db:
        if st.button(label="Connect",key="url_db_connect"):
            st.session_state.db_loc = url_db
            try:
                db_location = st.session_state.db_loc

                engine = create_engine(location=db_location, echo=False)

                st.session_state.engine = engine

            except Exception as e:
                st.error(f"Failed to connect to database with the provided URL: {str(e)}")


    # Return the database name (+basic info) and the list of database tables
    if st.session_state.engine is not None:

        db_info = get_db_info(st.session_state.engine)

        st.session_state.tables_list = db_info["table_names"]
        
        if st.session_state.tables_list:
            st.write("Available Tables")
            st.write(st.session_state.tables_list)
        elif not st.session_state.tables_list:
            st.write("No tables found")
    
    
if __name__ == "__main__":
    main()