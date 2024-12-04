import os
import sys
from pathlib import Path

import credentials

PROJECT_ROOT = Path(__file__).resolve().parent
RAW_WISH_LIST_DATA_PATH = (
    PROJECT_ROOT / "backend/app/comet_predictor/data_wish_list/raw_parsed_wish_list.csv"
)

WISH_LIST_DATA_PATH = (
    PROJECT_ROOT / "backend/app/comet_predictor/data_wish_list/parsed_wish_list.csv"
)
TEST_WISH_LIST_DATA_PATH = (
    PROJECT_ROOT / "backend/tests/comet_predictor/test_data/test_data_wish_list.csv"
)

TEST_PROFILE_WISH_LIST_DATA_PATH = (
    PROJECT_ROOT
    / "backend/tests/comet_predictor/test_data/test_profile_data_wish_list.csv"
)

COMET_HELPER_DATA_PATH = PROJECT_ROOT / "backend/app/comet_helper/data"

sys.path.append(PROJECT_ROOT)
os.environ["OPENAI_API_KEY"] = credentials.OPENAI_API_KEY

ANCHOR = True
