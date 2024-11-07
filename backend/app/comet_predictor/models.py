# User inputs from the streamlit app:
USER_PROFILE_INPUT = {}

# Parsing user input from streamlit, we get:
PARSED_PROFILE = {
    "section 1": "DROIT",
    "section 2": "SC. POLITIQUES RI",
    "international": 0,
    "relative overall average": 3,
    "absolute value overall average": 4,
    "french grade": 4,
}

# After having it parsed, we get:
POSSIBLE_WISHES = [
    {
        "place": "place 1",
        "institution": "easy institution 1",
        "wish name": "easy wish name 1",
        "number of spots": 972,
        "admission percentage": 99,
        "section 1": "DROIT",
        "section 2": "SC. POLITIQUES RI",
        "international": 0,
        "relative overall average": 0,
        "absolute value overall average": 0,
        "french grade": 0,
    },
    {
        "place": "place 3",
        "institution": "medium institution 2",
        "wish name": "medium wish name 2",
        "number of spots": 300,
        "admission percentage": 50,
        "section 1": "DROIT",
        "section 2": "SC. POLITIQUES RI",
        "international": 0,
        "relative overall average": 3,
        "absolute value overall average": 4,
        "french grade": 3,
    },
]
IMPOSSIBLE_WISHES = [
    {
        "place": "place 2",
        "institution": "very selective institution 2",
        "wish name": "very selective wish name 2",
        "number of spots": 10,
        "admission percentage": 1,
        "section 1": "DROIT",
        "section 2": "SC. POLITIQUES RI",
        "international": 1,
        "relative overall average": 5,
        "absolute value overall average": 5,
        "french grade": 5,
    }
]
