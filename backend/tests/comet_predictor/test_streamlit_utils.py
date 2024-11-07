from unittest.mock import patch

from backend.app.comet_predictor.old_version.models import (
    PARSED_CLEANED_EXAMPLE_USER,
    STREAMLIT_EXAMPLE_USER_INPUT,
)
from backend.app.comet_predictor.streamlit_utils import convert_to_example_format
from frontend.streamlit.pages.wish_list_predictor_page import streamlit_user_input


# Mocking the Streamlit UI components
def test_streamlit_user_input():
    with patch("streamlit.selectbox") as mock_selectbox, patch(
        "streamlit.multiselect"
    ) as mock_multiselect, patch("streamlit.slider") as mock_slider, patch(
        "streamlit.button"
    ) as mock_button:

        # Mock the values that users would select in the Streamlit app
        mock_selectbox.side_effect = ["DROIT", "SC. POLITIQUES RI"]
        mock_multiselect.return_value = ["HLP", "HGGSP", "SES"]
        mock_slider.side_effect = [15, 15]
        mock_button.return_value = True

        # Call the actual function
        responses = streamlit_user_input()

        # Verify that the responses match the expected output
        assert (
            responses == STREAMLIT_EXAMPLE_USER_INPUT
        ), f"Test failed! Expected {STREAMLIT_EXAMPLE_USER_INPUT}, but got {responses}"


def test_convert_to_example_format():

    actual_output = convert_to_example_format(STREAMLIT_EXAMPLE_USER_INPUT)

    assert (
        actual_output == PARSED_CLEANED_EXAMPLE_USER
    ), f"Test failed! Expected {PARSED_CLEANED_EXAMPLE_USER}, but got {actual_output}"


# Example of running the test
if __name__ == "__main__":
    test_convert_to_example_format()
