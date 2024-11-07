# User inputs from the streamlit app:
USER_PROFILE_INPUT = {}

# Parsing user input from streamlit, we get:
PARSED_PROFILE = {
    "section 1": "DROIT",
    "section 2": "SC. POLITIQUES RI",
    "subjects 1": ["SES"],
    "subjects 2": "[]",
    "subjects 3": "[]",
    "international": 0,
    "relative overall average": 3,
    "absolute value overall average": 4,
    "french grade": 4,
}

# After having it parsed, we get:
POSSIBLE_WISHES = [
    {
        "place": "place 1",
        "institution": "easy institution",
        "wish name": "easy wish name 1",
        "number of spots": 972,
        "admission percentage": 99,
        "section 1": "DROIT",
        "section 2": "SC. POLITIQUES RI",
        "subjects 1": "[]",
        "subjects 2": "[]",
        "subjects 3": "[]",
        "international": 0,
        "relative overall average": 0,
        "absolute value overall average": 0,
        "french grade": 0,
    }
]
IMPOSSIBLE_WISHES = [
    {
        "place": "place 2",
        "institution": "very selective institution grade trigger",
        "wish name": "very selective wish name 2",
        "number of spots": 10,
        "admission percentage": 1,
        "section 1": "DROIT",
        "section 2": "SC. POLITIQUES RI",
        "subjects 1": "[]",
        "subjects 2": "[]",
        "subjects 3": "[]",
        "international": 1,
        "relative overall average": 5,
        "absolute value overall average": 5,
        "french grade": 5,
    },
    {
        "place": "place 3",
        "institution": "very selective institution subject trigger",
        "wish name": "very selective wish name 2",
        "number of spots": 10,
        "admission percentage": 1,
        "section 1": "DROIT",
        "section 2": "SC. POLITIQUES RI",
        "subjects 1": "['Maths', 'MATHS COMPLEMENTAIRES']",
        "subjects 2": "['SES']",
        "subjects 3": "[]",
        "international": 0,
        "relative overall average": 0,
        "absolute value overall average": 0,
        "french grade": 0,
    },
]
