import os

from backend.app.comet_predictor.generator import generate_possible_wishes
from backend.app.comet_predictor.models import (
    PARSED_PROFILE,
    POSSIBLE_WISHES,
    IMPOSSIBLE_WISHES,
)


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


def test__hard_requirement_parser():
    pass
