
import os

from dotenv import load_dotenv
from playwright.sync_api import expect


load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def test_open_agnos(page):
    # ============================================================
    # Verify that the Agnos AI Dashboard application
    # can be opened successfully.
    # ============================================================

    # Navigate to the Agnos AI Dashboard page.
    page.goto(f"{BASE_URL}/ai_dashboard")

    # ============================================================
    # Verify that the application has loaded successfully.
    # ============================================================

    expect(page.locator("body")).to_be_visible()

    # ============================================================
    # Verify that the browser reached the expected application.
    # ============================================================

    expect(page).to_have_url(f"{BASE_URL}/ai_dashboard/login")

    # Display application information.
    print(f"Application URL: {page.url}")
    print(f"Page title: {page.title()}")
