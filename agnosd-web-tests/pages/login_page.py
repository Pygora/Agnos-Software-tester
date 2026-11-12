from playwright.sync_api import Page

from config import BASE_URL


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # ========================================================
        # LOGIN FORM LOCATORS
        # ========================================================

        self.email_input = page.locator("#Email")
        self.password_input = page.locator("#password")

        self.sign_in_button = page.get_by_role(
            "button", name="Sign in"
        )

    # ========================================================
    # NAVIGATION METHODS
    # ========================================================

    def navigate(self):
        # Navigate to the login page.
        self.page.goto(
            f"{BASE_URL}/ai_dashboard"
        )

    # ========================================================
    # LOGIN METHODS
    # ========================================================

    def login(self, email: str, password: str):
        # Enter the email address.
        self.email_input.fill(email)

        # Enter the password.
        self.password_input.fill(password)

        # Click the Sign in button.
        self.sign_in_button.click()