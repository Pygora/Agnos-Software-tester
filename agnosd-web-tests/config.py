
import os
from pathlib import Path

from dotenv import load_dotenv


# ============================================================
# Load environment variables from the project root.
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE, override=True)


# ============================================================
# Application configuration.
# ============================================================

BASE_URL = os.getenv("BASE_URL")


# ============================================================
# Login credentials.
# ============================================================

TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")
INVALID_LOGIN_PASSWORD = os.getenv("INVALID_LOGIN_PASSWORD")


# ============================================================
# Signup credentials.
# ============================================================

SIGNUP_TEST_PASSWORD = os.getenv("SIGNUP_TEST_PASSWORD")


# ============================================================
# Verify that required environment variables are configured.
# ============================================================

required_variables = {
    "BASE_URL": BASE_URL,
    "TEST_EMAIL": TEST_EMAIL,
    "TEST_PASSWORD": TEST_PASSWORD,
    "SIGNUP_TEST_PASSWORD": SIGNUP_TEST_PASSWORD,
}

missing_variables = [
    name for name, value in required_variables.items()
    if not value
]

if missing_variables:
    raise RuntimeError(
        f"Missing environment variables: {', '.join(missing_variables)}. "
        f"Check your .env file at: {ENV_FILE}"
    )


# ============================================================
# Status filter test data.
# ============================================================

TEST_STATUS_FILTERS = os.getenv(
    "TEST_STATUS_FILTERS", ""
).split(",")


# ============================================================
# Triage filter test data.
# ============================================================

TEST_TRIAGE_FILTERS = os.getenv(
    "TEST_TRIAGE_FILTERS", ""
).split(",")


# ============================================================
# Channel filter test data.
# ============================================================

TEST_CHANNEL_FILTERS = os.getenv(
    "TEST_CHANNEL_FILTERS", ""
).split(",")

TEST_INDIVIDUAL_CHANNELS = os.getenv(
    "TEST_INDIVIDUAL_CHANNELS", ""
).split(",")


# ============================================================
# Date filter test data.
# ============================================================

TEST_DATE_FILTER = os.getenv("TEST_DATE_FILTER")