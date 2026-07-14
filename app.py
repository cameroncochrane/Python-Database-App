# App frontend (Streamlit):

# Base modules:
import sys
from pathlib import Path
import streamlit as st
import pandas as pd


from db.engine import create_engine


def main():
    st.title("Database Exploration")


if __name__ == "__main__":
    main()