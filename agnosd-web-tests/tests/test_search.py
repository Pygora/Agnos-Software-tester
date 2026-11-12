from playwright.sync_api import expect

from config import TEST_EMAIL, TEST_PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


# ============================================================
# SEARCH TESTS
# ============================================================

def test_search_no_matching_record(page):
    # ============================================================
    # Verify that searching for a keyword with no matching
    # diagnosis records displays the empty state.
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
    # Search for a keyword with no matching records.
    # ============================================================

    # Enter a keyword that should not match any records.
    keyword = "NoMatchingPatient12345"
    dashboard_page.search(keyword)

    # ============================================================
    # Verify the search results.
    # ============================================================

    # Verify that the search keyword remains in the input.
    expect(
        dashboard_page.search_input
    ).to_have_value(keyword)

    # Verify that the empty diagnosis state is displayed.
    expect(
        page.get_by_text(
            "ยังไม่มีข้อมูลการวินิจฉัย",
            exact=True
        )
    ).to_be_visible()