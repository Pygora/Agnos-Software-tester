from playwright.sync_api import expect

from config import BASE_URL, TEST_EMAIL, TEST_PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


# ============================================================
# LOGOUT TESTS
# ============================================================

def test_logout_success(page):
    # ============================================================
    # Verify that a user can log out successfully.
    # ============================================================

    # Initialize page objects.
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Navigate to the login page.
    login_page.navigate()

    # Log in using valid credentials.
    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    # Verify that the dashboard is accessible.
    expect(
        dashboard_page.diagnosis_list_button
    ).to_be_visible()

    # ============================================================
    # Verify that the user is redirected to the login page.
    # ============================================================

    # Log out.
    dashboard_page.logout()

    # Verify that the login form is displayed.
    expect(login_page.email_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()


def test_dashboard_access_after_logout(page):
    # ============================================================
    # Verify that logged-out users cannot access the dashboard
    # by directly opening its URL.
    # ============================================================

    # Initialize page objects.
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Navigate to the login page.
    login_page.navigate()

    # Log in using valid credentials.
    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    # Verify that the dashboard is accessible.
    expect(
        dashboard_page.diagnosis_list_button
    ).to_be_visible()

    # ============================================================
    # Log out and attempt to access the dashboard directly.
    # ============================================================

    # Log out.
    dashboard_page.logout()

    # Navigate directly to the dashboard URL.
    page.goto(f"{BASE_URL}/ai_dashboard")

    # ============================================================
    # Verify that access to the dashboard is restricted.
    # ============================================================

    # Verify that the user is redirected to the login page.
    expect(page).to_have_url(
        f"{BASE_URL}/ai_dashboard/login"
    )

    # Verify that the login form is displayed.
    expect(login_page.email_input).to_be_visible()

    # Verify that dashboard content is inaccessible.
    expect(
        dashboard_page.diagnosis_list_button
    ).not_to_be_visible()
