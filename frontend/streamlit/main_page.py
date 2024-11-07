import os
import sys

import streamlit as st
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
sys.path.append(os.getenv("BACKEND_PATH"))
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
