def convert_to_example_format(responses):
    """
    Converts the Streamlit form responses into the format of PARSED_CLEANED_EXAMPLE_USER.
    """
    # Initialize the result with all subjects set to 0 by default
    example_user = {
        "FILIERE 1": responses.get("FILIERE 1", "None"),
        "FILIERE 2": responses.get("FILIERE 2", "None"),
        "INTERNATIONAL/ANGLAIS": 0,
        "Maths": 0,
        "PC": 0,
        "SVT": 0,
        "NSI": 0,
        "HLP": 0,
        "LLCE": 0,
        "AMC": 0,
        "HGGSP": 0,
        "SES": 0,
        "ARTS PLASTIQUES": 0,
        "DROIT ET GRANDS ENJEUX": 0,
        "MATHS COMPLEMENTAIRES": 0,
        "MATHS EXPERTES": 0,
        "STMG": 0,
        "moyenne": 0,
        "moyenne générale": 15,
        "moyenne de français": 15,
    }

    # Update the subjects selected by the user
    selected_subjects = responses.get("Selected Subjects", [])

    for subject in selected_subjects:
        if subject in example_user:
            example_user[subject] = 1

    # Add the "moyenne" value based on "moyenne générale" and "moyenne de français"
    example_user["moyenne"] = 1  # We assume >= moyenne as 1 based on provided input
    example_user["moyenne generale"] = responses.get("moyenne générale", 0)
    example_user["moyenne de français"] = responses.get("moyenne de français", 0)

    return example_user
