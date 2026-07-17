# App frontend (Streamlit):

# Base modules:
import sys
from pathlib import Path
import streamlit as st
import pandas as pd

from db.engine import create_engine


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


    # App layout
    st.title("Database Exploration")

    st.session_state.db_loc = st.text_input("Database Location", placeholder="Enter the path to your database")

    if st.button("Connect"):
        try:
            if st.session_state.db_loc is not None:
                
            engine = 


if __name__ == "__main__":
    main()