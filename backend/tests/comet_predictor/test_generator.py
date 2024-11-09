import os

import pandas as pd
from dotenv import load_dotenv

from backend.app.comet_predictor.generator import generate_possible_wishes
from backend.app.comet_predictor.models import (
    PARSED_PROFILE,
    POSSIBLE_WISHES,
    IMPOSSIBLE_WISHES,
)

load_dotenv()


def test_generate_possible_wishes():

    possible_wishes, impossible_wishes = generate_possible_wishes(
        PARSED_PROFILE, requirement_file_path=os.environ["TEST_WISH_LIST_DATA_PATH"]
    )

    for wish in POSSIBLE_WISHES:
        assert (
            wish in possible_wishes
        ), "Error with incorrect parsing of possible wishes."

    for wish in IMPOSSIBLE_WISHES:
        assert (
            wish in impossible_wishes
        ), "Error with incorrect parsing of impossible wishes."


def test_test_data_wish_list():
    test_df = pd.read_csv(os.environ["TEST_WISH_LIST_DATA_PATH"])
    prod_df = pd.read_csv(os.environ["WISH_LIST_DATA_PATH"])

    # Check for column equality (ignoring order)
    assert set(test_df.columns) == set(
        prod_df.columns
    ), "Error likely due to outdated test data or column mismatch."

    # Optionally, check column order if required
    assert list(test_df.columns) == list(
        prod_df.columns
    ), "Column order mismatch in test data."
