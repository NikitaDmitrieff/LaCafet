import os
import sys

import streamlit as st

sys.path.append(os.getcwd())

import config

config.ANCHOR

# Load environment variables from the .env file
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
