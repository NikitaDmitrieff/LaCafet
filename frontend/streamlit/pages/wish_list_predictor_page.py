import os

import streamlit as st

from backend.app.comet_predictor.streamlit_utils import convert_to_example_format

st.markdown(f"{os.getcwd()}")
st.markdown("# Wish list predictor")
# Page and Sidebar titles
st.sidebar.markdown("# Wish list predictor")


def streamlit_user_input():
    # Dictionary to store the user responses
    responses = {}

    st.title("Enter Your Academic and Subject Data")

    # Filière 1 and Filière 2
    filiere_1_options = [
        "DROIT",
        "SC.POLITIQUE RI",
        "HISTOIRE",
        "HUMANITES",
        "ECONOMIE",
        "ECONOMIE GESTION",
        "MATHEMATIQUES",
        "COMMERCE",
        "None",  # In place of 0
    ]

    filiere_2_options = [
        "SC. POLITIQUES RI",
        "SCIENCES SOCIALES",
        "PHILOSOPHIE",
        "HISTOIRE",
        "LANGUES",
        "None",  # In place of 0
        "HUMANITES",
        "ECONOMIE",
        "GESTION",
        "MATHEMATIQUES",
        "DROIT",
        "INFO. - DATA SCIENCE - IA",
        "MNGT GENERAL",
        "LUXE MODE",
        "DIGITAL E-BUSINESS",
        "INGENIEUR",
    ]

    responses["FILIERE 1"] = st.selectbox("Filière 1", filiere_1_options)
    responses["FILIERE 2"] = st.selectbox("Filière 2", filiere_2_options)

    # Subject options to be selected with multi-select
    subject_options = [
        "INTERNATIONAL/ANGLAIS",
        "Maths",
        "PC",
        "SVT",
        "NSI",
        "HLP",
        "LLCE",
        "AMC",
        "HGGSP",
        "SES",
        "ARTS PLASTIQUES",
        "DROIT ET GRANDS ENJEUX",
        "MATHS COMPLEMENTAIRES",
        "MATHS EXPERTES",
        "STMG",
    ]

    # Multi-select box to allow users to select up to 3 subjects
    responses["Selected Subjects"] = st.multiselect(
        "Select up to 3 Subjects",
        options=subject_options,
        default=None,
        max_selections=3,
    )

    # Handling for "moyenne" fields with sliders and text inputs
    st.subheader("moyenne générale Thresholds")
    responses["moyenne générale"] = st.slider(
        "Moyenne générale (0 to 20)",
        0,
        20,
    )
    responses["moyenne de français"] = st.slider(
        "Moyenne de français (0 to 20)",
        0,
        20,
    )

    # Submit button
    if st.button("Submit"):
        return convert_to_example_format(responses)
