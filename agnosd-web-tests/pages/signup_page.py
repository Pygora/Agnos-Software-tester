from playwright.sync_api import Page

from config import BASE_URL


class SignupPage:

    def __init__(self, page: Page):
        self.page = page

        # ========================================================
        # SIGNUP FORM LOCATORS
        # ========================================================

        self.email_input = page.locator("#Email")

        self.password_inputs = page.locator("#password")
        self.password_input = self.password_inputs.nth(0)
        self.confirm_password_input = self.password_inputs.nth(1)

        self.confirm_button = page.get_by_role(
            "button", name="Confirm"
        )

    # ========================================================
    # NAVIGATION METHODS
    # ========================================================

    def navigate(self):
        # Navigate to the signup page.
        self.page.goto(
            f"{BASE_URL}/ai_dashboard/agnos/sign_up"
        )

    # ========================================================
    # SIGNUP METHODS
    # ========================================================

    def fill_signup_form(self, email, password, confirm_password):
        # Fill in the email address.
        self.email_input.fill(email)

        # Fill in the password.
        self.password_input.fill(password)

        # Fill in the confirmation password.
        self.confirm_password_input.fill(confirm_password)

    def submit(self):
        # Submit the signup form.
        self.confirm_button.click()