import os

import pandas as pd
import streamlit as st

from backend.app.comet_predictor.generator_utils import (
    get_requirements_df,
    EXAMPLE_USER,
    get_profile_df,
    _preliminary_cleaning,
    _parse_grade_requirements,
)

st.sidebar.markdown("# Wish list under the hood")
st.markdown("# Wish list under the hood")


requirements = get_requirements_df()
profiles = get_profile_df()

if st.checkbox("Requirements"):
    requirements

if st.checkbox("Profiles"):
    profiles

if st.checkbox("Show profile intermediate steps"):

    # Raw dictionnary
    st.markdown("### 1. Raw DF from user")
    raw_df = pd.DataFrame([EXAMPLE_USER])
    raw_df

    # Quick cleaning
    cleaned_df = _preliminary_cleaning(raw_df)
    st.markdown("### 2. Cleaning: replace NaN, convert to integers...")
    cleaned_df

    # Update grade requirements
    st.markdown("### 3. Grade processing")
    parsed_df = _parse_grade_requirements(cleaned_df.copy())
    parsed_df

    # Conclude
    st.markdown("### Overview")
    concatenated_df = pd.concat([raw_df, cleaned_df, parsed_df])
    concatenated_df

if st.checkbox("Show requirements intermediate steps"):

    # Raw dictionnary
    st.markdown("### 1. Raw DF from database")
    raw_df = pd.read_csv(os.getenv("DATA_WISH_LIST_PATH"))
    raw_df

    # Quick cleaning
    cleaned_df = _preliminary_cleaning(raw_df)
    st.markdown("### 2. Cleaning: replace NaN, convert to integers...")
    cleaned_df

    # Update grade requirements
    st.markdown("### 3. Grade processing")
    parsed_df = _parse_grade_requirements(cleaned_df)
    parsed_df
