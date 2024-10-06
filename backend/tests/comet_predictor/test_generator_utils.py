import pandas as pd

from backend.app.comet_predictor.generator_utils import (
    _parse_grade_requirements,
    _preliminary_cleaning,
)
from backend.app.comet_predictor.models import (
    RAW_EXAMPLE_USER,
    CLEANED_EXAMPLE_USER,
    PARSED_CLEANED_EXAMPLE_USER,
)


def test__preliminary_cleaning():
    # Example input as dataframe
    df = pd.DataFrame([RAW_EXAMPLE_USER])

    # Clean and process the dataframe
    processed_df = _preliminary_cleaning(df)

    # Compare results with expected values
    for column, expected_value in CLEANED_EXAMPLE_USER.items():
        assert (
            processed_df.iloc[0][column] == expected_value
        ), f"Mismatch in column {column}: expected {expected_value}, got {processed_df.iloc[0][column]}"


def test__parse_grade_requirements():

    expected_dict = pd.DataFrame([PARSED_CLEANED_EXAMPLE_USER])

    # Run the conversion function
    actual_output = _parse_grade_requirements(pd.DataFrame([CLEANED_EXAMPLE_USER]))

    # Assert the output matches the expected values
    assert (
        actual_output.iloc[0].to_dict() == expected_dict.iloc[0].to_dict()
    ), f"Test failed! Expected {expected_dict}, but got {actual_output}"
