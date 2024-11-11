import json
from typing import List, Tuple

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
                "relative overall average",
                "absolute value overall average",
                "french grade",
                "math level",
            ]:
                if profile[requirement_name] < requirement_value:
                    can_apply = False
                    break

            elif requirement_name in ["subjects 1"]:
                for subject in json.loads(requirement_value.replace("'", '"')):
                    if subject not in profile[requirement_name]:
                        can_apply = False
                        break

            elif requirement_name in ["section 1"]:
                section_match = any(
                    section in [profile["section 1"], profile["section 2"]]
                    for section in [row["section 1"], row["section 2"]]
                )

                if not section_match:
                    can_apply = False
                    break

        if can_apply:
            possible_wishes.append(row.to_dict())
        else:
            impossible_wishes.append(row.to_dict())

    return possible_wishes, impossible_wishes


def generate_possible_wishes(
    profile: dict, requirement_file_path: str = "data_wish_list/parsed_wish_list.csv"
) -> Tuple[List[dict], List[dict]]:
    """
    Main function for retrieving the possible wishes for a certain profile:
        Calls hard_requirement parser

    Args:
        profile: dict with the user's grades and sections
        requirement_file_path: str leading to the requirement csv file
    returns:
        possible_wishes: List
        impossible_wishes: List
    """

    requirements_df = pd.read_csv(requirement_file_path)

    # Parse though hard grade requirements
    possible_wishes, impossible_wishes = _hard_requirement_parser(
        requirements_df=requirements_df, profile=profile
    )

    return possible_wishes, impossible_wishes
