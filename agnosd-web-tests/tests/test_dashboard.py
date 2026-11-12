
import os

from dotenv import load_dotenv
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


load_dotenv()

TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")


def test_diagnosis_list_button_click(page):
    # ============================================================
    # Verify that a user can access the Diagnosis List
    # after logging in successfully.
    # ============================================================

    # Verify that login credentials are configured.
    assert TEST_EMAIL, "TEST_EMAIL is missing from .env"
    assert TEST_PASSWORD, "TEST_PASSWORD is missing from .env"

    # Initialize page objects.
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # ============================================================
    # Log in to the Agnos AI Dashboard.
    # ============================================================

    # Navigate to the login page.
    login_page.navigate()

    # Enter valid login credentials.
    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    # ============================================================
    # Verify that the Diagnosis List button is visible.
    # ============================================================

    expect(
        dashboard_page.diagnosis_list_button
    ).to_be_visible()

    # ============================================================
    # Verify that a user can click the Diagnosis List button.
    # ============================================================

    # Click the Diagnosis List button.
    dashboard_page.open_diagnosis_list()

    # Verify that the Diagnosis List button remains visible.
    expect(
        dashboard_page.diagnosis_list_button
    ).to_be_visible()
