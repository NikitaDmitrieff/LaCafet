import os
from typing import List, Dict

import pandas as pd

EXAMPLE_USER = {
    "FILIERE 1": "DROIT",
    "FILIERE 2": "SC. POLITIQUES RI",
    "INTERNATIONAL/ANGLAIS": 0,
    "Maths": 0,
    "PC": 0,
    "SVT": 0,
    "NSI": 0,
    "HLP": 2,
    "LLCE": 0,
    "AMC": 0,
    "HGGSP": 1,
    "SES": 2,
    "ARTS PLASTIQUES": 0,
    "DROIT ET GRANDS ENJEUX": 3,
    "MATHS COMPLEMENTAIRES": 0,
    "MATHS EXPERTES": 0,
    "STMG": 0,
    ">> moyenne": "X",
    ">= moyenne": "X",
    "<= moyenne": 0,
    "<< moyenne": 0,
    "moyenne générale <10": 0,
    "moyenne générale entre 10 et 12": 0,
    "moyenne générale entre 12 et 14": 1,
    "moyenne générale entre 14 et 16": 0,
    "moyenne générale >16": 0,
    "moyenne de français <10": 0,
    "moyenne de français entre 10 et 12": 0,
    "moyenne de français entre 12 et 14": 1,
    "moyenne de français entre 14 et 16": 0,
    "moyenne de français >16": 0,
    "moyenne de français >18": 0,
}

integers_columns_to_select = [
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
    ">> moyenne",
    ">= moyenne",
    "<= moyenne",
    "<< moyenne",
    "moyenne générale <10",
    "moyenne générale entre 10 et 12",
    "moyenne générale entre 12 et 14",
    "moyenne générale entre 14 et 16",
    "moyenne générale >16",
    "moyenne de français <10",
    "moyenne de français entre 10 et 12",
    "moyenne de français entre 12 et 14",
    "moyenne de français entre 14 et 16",
    "moyenne de français >16",
    "moyenne de français >18",
]


def _process_grade_requirements_one_row(row: Dict) -> Dict:
    result = {}

    # Handle "moyenne" thresholds
    if row.get(">> moyenne", 0) == 1:
        result["moyenne"] = 0
    elif row.get(">= moyenne", 0) == 1:
        result["moyenne"] = 1
    elif row.get("<= moyenne", 0) == 1:
        result["moyenne"] = 2
    elif row.get("<< moyenne", 0) == 1:
        result["moyenne"] = 3

    # Process "moyenne generale"
    if row.get("moyenne générale >16", 0) == 1:
        result["moyenne generale"] = 17
    elif row.get("moyenne générale entre 14 et 16", 0) == 1:
        result["moyenne generale"] = 15
    elif row.get("moyenne générale entre 12 et 14", 0) == 1:
        result["moyenne generale"] = 13
    elif row.get("moyenne générale entre 10 et 12", 0) == 1:
        result["moyenne generale"] = 11
    elif row.get("moyenne générale <10", 0) == 1:
        result["moyenne generale"] = 9
    else:
        result["moyenne generale"] = 0  # Default value if no range is selected

    # Process "moyenne de français"
    if row.get("moyenne de français >18", 0) == 1:
        result["moyenne de français"] = 19
    elif row.get("moyenne de français >16", 0) == 1:
        result["moyenne de français"] = 17
    elif row.get("moyenne de français entre 14 et 16", 0) == 1:
        result["moyenne de français"] = 15
    elif row.get("moyenne de français entre 12 et 14", 0) == 1:
        result["moyenne de français"] = 13
    elif row.get("moyenne de français entre 10 et 12", 0) == 1:
        result["moyenne de français"] = 11
    elif row.get("moyenne de français <10", 0) == 1:
        result["moyenne de français"] = 9
    else:
        result["moyenne de français"] = 0  # Default value if no range is selected

    return result


def _parse_grade_requirements(raw_df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts a DataFrame of natural language descriptions for "moyenne" ranges
    into concise numerical values for each row.

    Args:
        raw_df (pd.DataFrame): DataFrame where each row contains natural language
        descriptions for "moyenne" ranges.

    Returns:
        pd.DataFrame: A DataFrame with concise, numerical values for "moyenne generale"
        and "moyenne de français".
    """
    # Select only the specific columns to process
    selected_columns = [
        ">> moyenne",
        ">= moyenne",
        "<= moyenne",
        "<< moyenne",
        "moyenne générale <10",
        "moyenne générale entre 10 et 12",
        "moyenne générale entre 12 et 14",
        "moyenne générale entre 14 et 16",
        "moyenne générale >16",
        "moyenne de français <10",
        "moyenne de français entre 10 et 12",
        "moyenne de français entre 12 et 14",
        "moyenne de français entre 14 et 16",
        "moyenne de français >16",
        "moyenne de français >18",
    ]

    # Filter the DataFrame to keep only the relevant columns
    filtered_df = raw_df[selected_columns]

    # Apply the processing function to each row
    parsed_data = filtered_df.apply(_process_grade_requirements_one_row, axis=1)

    # Convert the list of dictionaries into a DataFrame
    result_df = pd.DataFrame(parsed_data.tolist())

    # Drop the original selected columns from the original DataFrame
    raw_df = raw_df.drop(columns=selected_columns)

    # Insert the new processed columns back into the DataFrame
    raw_df = pd.concat([raw_df, result_df], axis=1)

    return raw_df


def _preliminary_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """
    Takes raw DF and makes it digestible:
        - Replace NaN
        - Drop unnecessary column
        - Process Xs
        - Convert to integers
    """

    # Replace NaN values with 0
    df = df.fillna(0)

    # Drop the unnamed column & replace "X"s with 1s
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    df.replace("X", 1, inplace=True)

    # Remove 2s and 3s
    df = df.replace(2, 1).replace(3, 1)

    # Convert to integers
    df[integers_columns_to_select] = df[integers_columns_to_select].astype(int)
    return df


def _process_dataframe(raw_df: pd.DataFrame) -> pd.DataFrame:
    """
    For both requirements and profiles. From raw dataframe to cleaned dataframe ready for use.
    """

    # Quick cleaning
    cleaned_df = _preliminary_cleaning(raw_df)

    # Update grade requirements
    parsed_df = _parse_grade_requirements(cleaned_df)

    return parsed_df


def user_prompt_multiple_choice():
    # Dictionary to store the user responses
    responses = {}

    # List of questions and corresponding options
    questions = {
        "Filière 1": [
            "DROIT",
            "SC.POLITIQUE RI",
            "HISTOIRE",
            "HUMANITES",
            "ECONOMIE",
            "ECONOMIE GESTION",
            "ÉCONOMIE GESTION",
            "MATHEMATIQUES",
            "COMMERCE",
            0,
        ],
        "Filière 2": [
            "SC. POLITIQUES RI",
            "SCIENCES SOCIALES",
            "PHILOSOPHIE",
            "HISTOIRE",
            "LANGUES",
            0,
            "HUMANITES",
            "ECONOMIE",
            "GESTION",
            "ÉCONOMIE GESTION",
            "MATHEMATIQUES",
            "DROIT",
            "INFO. - DATA SCIENCE - IA",
            "MNGT GENERAL",
            "LUXE MODE",
            "DIGITAL E-BUSINESS",
            "INGENIEUR",
        ],
    }

    # Iterate through the questions and provide multiple-choice options
    for question, options in questions.items():
        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        # Keep prompting the user until a valid choice is made
        while True:
            try:
                choice = int(input("Please enter the number of your choice: "))
                if 1 <= choice <= len(options):
                    responses[question] = options[choice - 1]
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Print the responses
    print("\nYour responses:")
    for question, answer in responses.items():
        print(f"{question}: {answer}")

    return responses


def get_requirements_df(
    filepath: str = os.getenv("DATA_WISH_LIST_PATH"),
) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return _process_dataframe(raw_df=df)


def get_profile_df(example_users: List[Dict] = None) -> pd.DataFrame:
    """
    Main function:
        Takes users' outputs and parses them to return a clean, comparable dataframe.
        If has grade average > 14:
            - > 10 = 1
            - > 12 = 1
            - > 14 = 1
            - > 16 = 0
    """

    if example_users is None:
        example_users = [EXAMPLE_USER]

    return _process_dataframe(raw_df=pd.DataFrame(example_users))
