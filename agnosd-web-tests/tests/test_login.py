from playwright.sync_api import expect

from config import (
    BASE_URL,
    TEST_EMAIL,
    TEST_PASSWORD,
    INVALID_LOGIN_PASSWORD,
)
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


# ============================================================
# LOGIN TESTS
# ============================================================

def test_login_success(page):
    # ============================================================
    # Verify that a user can log in using valid credentials.
    # ============================================================

    # Initialize page objects.
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Navigate to the login page.
    login_page.navigate()

    # Enter valid credentials and submit.
    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    # ============================================================
    # Verify that the dashboard is accessible.
    # ============================================================

    expect(
        dashboard_page.diagnosis_list_button
    ).to_be_visible()


def test_login_invalid_password(page):
    # ============================================================
    # Verify that login is rejected when the password is incorrect.
    # ============================================================

    # Initialize page objects.
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Navigate to the login page.
    login_page.navigate()

    # Use a valid email with an incorrect password.
    login_page.login(TEST_EMAIL, INVALID_LOGIN_PASSWORD)

    # Verify that the user remains on the login page.
    expect(page).to_have_url(
        f"{BASE_URL}/ai_dashboard/login"
    )

    # Verify that the login error message is displayed.
    expect(
        page.get_by_text(
            "Wrong email or password. Please try again"
        )
    ).to_be_visible()

    # Verify that dashboard content is not accessible.
    expect(
        dashboard_page.diagnosis_list_button
    ).not_to_be_visible()


def test_login_empty_credentials(page):
    # ============================================================
    # Verify that users cannot submit an empty login form.
    # ============================================================

    # Initialize the login page.
    login_page = LoginPage(page)

    # Navigate to the login page.
    login_page.navigate()

    # Verify that both credential fields are initially empty.
    expect(login_page.email_input).to_be_empty()
    expect(login_page.password_input).to_be_empty()

    # Verify that the Sign In button is disabled.
    expect(login_page.sign_in_button).to_be_disabled()