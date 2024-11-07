from typing import List

import pandas as pd


def _hard_requirement_parser(
    requirements_df: pd.DataFrame, profile: dict
) -> List[dict]:
    possible_wishes = []
    impossible_wishes = []

    for index, row in requirements_df.iterrows():

        can_apply = True
        for requirement_name, requirement_value in row.to_dict().items():

            if requirement_name in [
                "international",
                "relative overall average",
                "absolute value overall average",
                "french grade",
            ]:
                if profile[requirement_name] < requirement_value:
                    can_apply = False
                    break

        if can_apply:
            possible_wishes.append(row.to_dict())
        else:
            impossible_wishes.append(row.to_dict())

    return possible_wishes, impossible_wishes


def generate_possible_wishes(
    profile: dict, requirement_file_path: str = "data_wish_list/parsed_wish_list.csv"
) -> List[dict]:
    """
    Main function for retrieving the possible wishes for a certain profile:
        Calls hard_requirement parser

    Args:
        profile: dict with the user's grades and sections
        requirement_file_path: str leading to the requirement csv file
    """

    # Parse though hard requirements
    requirements_df = pd.read_csv(requirement_file_path)
    possible_wishes = _hard_requirement_parser(
        requirements_df=requirements_df, profile=profile
    )

    # Other parsing

    return possible_wishes
