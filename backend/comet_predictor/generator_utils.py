from typing import List, Dict

import pandas as pd

example_user = {
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
    "moyenne general < 10": 0,
    "moyenne general entre 10 et 12": 0,
    "moyenne general entre 12 et 14": 0,
    "moyenne general entre 14 et 16": 0,
    "moyenne general >16": 0,
    "moyenne de français < 10": 0,
    "moyenne de français entre 10 et 12": 0,
    "moyenne de français entre 12 et 14": 2,
    "moyenne de français entre 14 et 16": 1,
    "moyenne de français >16": 2,
    "moyenne de français >18": 1,
}
example_users = [example_user]

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
    "moyenne general < 10",
    "moyenne general entre 10 et 12",
    "moyenne general entre 12 et 14",
    "moyenne general entre 14 et 16",
    "moyenne general >16",
    "moyenne de français < 10",
    "moyenne de français entre 10 et 12",
    "moyenne de français entre 12 et 14",
    "moyenne de français entre 14 et 16",
    "moyenne de français >16",
    "moyenne de français >18",
]


def update_grade_requirements(df: pd.DataFrame) -> pd.DataFrame:
    # Define the columns to process for general grades and French grades
    general_columns = [
        "moyenne general < 10",
        "moyenne general entre 10 et 12",
        "moyenne general entre 12 et 14",
        "moyenne general entre 14 et 16",
        "moyenne general >16",
    ]

    french_columns = [
        "moyenne de français < 10",
        "moyenne de français entre 10 et 12",
        "moyenne de français entre 12 et 14",
        "moyenne de français entre 14 et 16",
        "moyenne de français >16",
        "moyenne de français >18",
    ]

    for index in range(1, len(general_columns)):
        high_col = general_columns[index]
        low_col = general_columns[index - 1]

        df[high_col] = df.apply(
            lambda row: (
                1 if row[low_col] == 1 or row[low_col] == "1" else row[high_col]
            ),
            axis=1,
        )

    for index in range(1, len(french_columns)):
        high_col = french_columns[index]
        low_col = french_columns[index - 1]

        df[high_col] = df.apply(
            lambda row: (1 if int(row[low_col]) == 1 else row[high_col]),
            axis=1,
        )

    return df


def process_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    For both requirements and profiles. From raw dataframe to cleaned dataframe ready for use.
    """

    # Replace NaN values with 0
    df = df.fillna(0)

    # Drop the unnamed column & replace "X"s with 1s
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    df.replace("X", 1, inplace=True)

    # Remove 2s and 3s
    df = df.replace(2, 0).replace(3, 0)

    # Convert to integers
    df[integers_columns_to_select] = df[integers_columns_to_select].astype(int)

    # Update grade requirements
    df = update_grade_requirements(df)

    return df


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


def prepare_csv(filepath: str = "data_wish_list/parsed_wish_list.csv") -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return process_dataframe(df=df)


def prepare_profile_dictionnary(example_users: List[Dict] = None):

    if example_users is None:
        example_users = [example_user]

    return process_dataframe(pd.DataFrame(example_users))


if __name__ == "__main__":
    list_of_profiles = [example_user]
