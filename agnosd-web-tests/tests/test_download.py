import re

from playwright.sync_api import expect

from config import TEST_EMAIL, TEST_PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_download_diagnosis_list(page):
    # ============================================================
    # Verify that a user can download the Diagnosis List as a CSV
    # file after logging in successfully.
    # ============================================================

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
    # Verify that the Diagnosis List is accessible.
    # ============================================================

    expect(
        dashboard_page.diagnosis_list_button
    ).to_be_visible()

    # ============================================================
    # Verify that the download confirmation popup is displayed.
    # ============================================================

    # Click the Download button.
    dashboard_page.click_download()

    # Verify the confirmation popup title.
    expect(
        dashboard_page.download_confirmation_title
    ).to_be_visible()

    # Verify the CSV download confirmation button.
    expect(
        dashboard_page.confirm_download_button
    ).to_be_visible()

    # ============================================================
    # Verify that the CSV download link is generated.
    # ============================================================

    # Verify that the confirmation button contains a download URL.
    expect(
        dashboard_page.confirm_download_button
    ).to_have_attribute("href", re.compile(r"^blob:"))

    # Retrieve the generated download URL.
    download_link = dashboard_page.confirm_download_button.get_attribute("href")

    # Verify the generated URL.
    assert download_link is not None and download_link.startswith("blob:"), (
        f"Expected a blob download URL, got: {download_link}"
    )

    print("CSV download link generated successfully.")
