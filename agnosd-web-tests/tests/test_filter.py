import pytest
from playwright.sync_api import expect

from config import (
    TEST_EMAIL,
    TEST_PASSWORD,
    TEST_STATUS_FILTERS,
    TEST_TRIAGE_FILTERS,
    TEST_CHANNEL_FILTERS,
    TEST_INDIVIDUAL_CHANNELS,
    TEST_DATE_FILTER,
)
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


# ============================================================
# Reusable login setup.
# ============================================================

def login_to_dashboard(page):
    # Initialize the login page.
    login_page = LoginPage(page)

    # Navigate to the login page.
    login_page.navigate()

    # Log in using valid credentials.
    login_page.login(TEST_EMAIL, TEST_PASSWORD)


# ============================================================
# STATUS FILTER TESTS
# ============================================================

@pytest.mark.parametrize("filter_name", TEST_STATUS_FILTERS)
def test_filter_by_status(page, filter_name):
    # ============================================================
    # Verify that a user can filter diagnosis cases by status.
    # ============================================================

    # Initialize the dashboard page.
    dashboard_page = DashboardPage(page)

    # Log in to the Agnos AI Dashboard.
    login_to_dashboard(page)

    # Verify that the Diagnosis List is accessible.
    expect(dashboard_page.diagnosis_list_button).to_be_visible()

    # ============================================================
    # Select the requested status filter.
    # ============================================================

    status_filters = {
        "Open": dashboard_page.select_open_filter,
        "In progress": dashboard_page.select_in_progress_filter,
        "Completed": dashboard_page.select_completed_filter,
    }

    status_filters[filter_name]()

    # Verify that the total cases label is visible.
    expect(dashboard_page.total_cases_label).to_be_visible()


# ============================================================
# TRIAGE FILTER TESTS
# ============================================================

@pytest.mark.parametrize("filter_name", TEST_TRIAGE_FILTERS)
def test_filter_by_triage(page, filter_name):
    # ============================================================
    # Verify that a user can filter diagnosis cases by triage level.
    # ============================================================

    # Initialize the dashboard page.
    dashboard_page = DashboardPage(page)

    # Log in to the Agnos AI Dashboard.
    login_to_dashboard(page)

    # Verify that the Diagnosis List is accessible.
    expect(dashboard_page.diagnosis_list_button).to_be_visible()

    # ============================================================
    # Select the requested triage filter.
    # ============================================================

    triage_filters = {
        "All": dashboard_page.select_all_triage_filter,
        "Self care": dashboard_page.select_self_care_filter,
        "Seek Medical": dashboard_page.select_seek_medical_filter,
        "Urgent": dashboard_page.select_urgent_filter,
        "Emergency": dashboard_page.select_emergency_filter,
    }

    triage_filters[filter_name]()

    # Verify that the total cases label is visible.
    expect(dashboard_page.total_cases_label).to_be_visible()


# ============================================================
# CHANNEL FILTER TESTS
# ============================================================

def test_channel_filter_default_all(page):
    # ============================================================
    # Verify that all channel options are selected by default.
    # ============================================================

    # Initialize the dashboard page.
    dashboard_page = DashboardPage(page)

    # Log in to the Agnos AI Dashboard.
    login_to_dashboard(page)

    # Verify that the Diagnosis List is accessible.
    expect(dashboard_page.diagnosis_list_button).to_be_visible()

    # Open the channel dropdown.
    dashboard_page.open_channel_dropdown()

    # Verify that every configured channel is selected.
    for channel_name in TEST_CHANNEL_FILTERS:
        assert dashboard_page.is_channel_selected(channel_name), (
            f"{channel_name} should be selected by default."
        )


@pytest.mark.parametrize("channel_name", TEST_INDIVIDUAL_CHANNELS)
def test_channel_filter_toggle_selection(page, channel_name):
    # ============================================================
    # Verify that a user can toggle individual channel selections.
    # ============================================================

    # Initialize the dashboard page.
    dashboard_page = DashboardPage(page)

    # Log in to the Agnos AI Dashboard.
    login_to_dashboard(page)

    # Verify that the Diagnosis List is accessible.
    expect(dashboard_page.diagnosis_list_button).to_be_visible()

    # Open the channel dropdown.
    dashboard_page.open_channel_dropdown()

    # Verify the initial channel selection.
    assert dashboard_page.is_channel_selected(channel_name), (
        f"{channel_name} should initially be selected."
    )

    # ============================================================
    # Verify that the channel can be deselected.
    # ============================================================

    # Uncheck the selected channel.
    dashboard_page.select_channel_option(channel_name)

    assert not dashboard_page.is_channel_selected(channel_name), (
        f"{channel_name} should be unchecked after clicking."
    )

    # ============================================================
    # Verify that the channel can be selected again.
    # ============================================================

    # Check the channel again.
    dashboard_page.select_channel_option(channel_name)

    assert dashboard_page.is_channel_selected(channel_name), (
        f"{channel_name} should be checked after clicking again."
    )


# ============================================================
# DATE FILTER TESTS
# ============================================================

def test_date_calendar_selection(page):
    # ============================================================
    # Verify that a user can select the configured date filter.
    # ============================================================

    # Initialize the dashboard page.
    dashboard_page = DashboardPage(page)

    # Log in to the Agnos AI Dashboard.
    login_to_dashboard(page)

    # Verify that the Diagnosis List is accessible.
    expect(dashboard_page.diagnosis_list_button).to_be_visible()

    # ============================================================
    # Verify that the date calendar can be opened.
    # ============================================================

    # Open the date filter.
    dashboard_page.open_date_calendar()

    # Verify that the configured date option is visible.
    expect(
        page.get_by_text(TEST_DATE_FILTER, exact=True)
    ).to_be_visible()

    # ============================================================
    # Verify that the configured date filter can be selected.
    # ============================================================

    # Select the configured date.
    if TEST_DATE_FILTER == "Today":
        dashboard_page.select_today_date()
    else:
        pytest.fail(
            f"Unsupported date filter: {TEST_DATE_FILTER}"
        )

    # Verify that the date menu is closed.
    expect(dashboard_page.date_picker).not_to_be_visible()

    # Verify that the configured date filter is displayed.
    expect(
        page.get_by_text(TEST_DATE_FILTER, exact=True)
    ).to_be_visible()