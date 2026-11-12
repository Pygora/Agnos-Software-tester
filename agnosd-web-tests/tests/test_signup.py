import uuid

from playwright.sync_api import expect

from config import TEST_EMAIL, SIGNUP_TEST_PASSWORD
from pages.signup_page import SignupPage


# ============================================================
# TEST CONFIGURATION
# ============================================================

EXISTING_EMAIL = TEST_EMAIL
TEST_PASSWORD = SIGNUP_TEST_PASSWORD


def generate_test_email():
    # Generate a unique email address for each registration test.
    return f"qa_test_{uuid.uuid4().hex[:6]}@gmail.com"


# ============================================================
# SIGNUP PAGE TESTS
# ============================================================

def test_signup_page_loads(page):
    # ============================================================
    # Verify that all signup form fields are displayed.
    # ============================================================

    # Initialize the signup page.
    signup_page = SignupPage(page)

    # Navigate to the signup page.
    signup_page.navigate()

    # Verify that all form elements are visible.
    expect(signup_page.email_input).to_be_visible()
    expect(signup_page.password_input).to_be_visible()
    expect(signup_page.confirm_password_input).to_be_visible()
    expect(signup_page.confirm_button).to_be_visible()


def test_signup_confirm_button_disabled_when_fields_empty(page):
    # ============================================================
    # Verify that the Confirm button is disabled when all
    # signup fields are empty.
    # ============================================================

    # Initialize the signup page.
    signup_page = SignupPage(page)

    # Navigate to the signup page.
    signup_page.navigate()

    # Verify that all fields are empty.
    expect(signup_page.email_input).to_be_empty()
    expect(signup_page.password_input).to_be_empty()
    expect(signup_page.confirm_password_input).to_be_empty()

    # Verify that the Confirm button is disabled.
    expect(signup_page.confirm_button).to_be_disabled()


def test_signup_invalid_email(page):
    # ============================================================
    # Verify that signup rejects an invalid email format.
    # ============================================================

    # Initialize the signup page.
    signup_page = SignupPage(page)

    # Navigate to the signup page.
    signup_page.navigate()

    # Enter an invalid email and valid passwords.
    signup_page.fill_signup_form(
        "not-an-email",
        "ValidPass123!",
        "ValidPass123!"
    )

    # Submit the signup form.
    signup_page.submit()

    # Verify that the email validation message is displayed.
    expect(
        page.get_by_text(
            "The email should be in the format 'test@example.com'",
            exact=True
        )
    ).to_be_visible()


def test_signup_short_password(page):
    # ============================================================
    # Verify that signup rejects a password that does not
    # meet the minimum password requirements.
    # ============================================================

    # Initialize the signup page.
    signup_page = SignupPage(page)

    # Navigate to the signup page.
    signup_page.navigate()

    # Enter a password that is too short.
    signup_page.fill_signup_form(
        "test@example.com",
        "123",
        "123"
    )

    # Submit the signup form.
    signup_page.submit()

    # Verify that the password validation message is displayed.
    expect(
        page.get_by_text(
            "The password must be at least 8 characters long and include at least one uppercase letter, one digit, and one special character.",
            exact=True
        )
    ).to_be_visible()


def test_signup_password_mismatch(page):
    # ============================================================
    # Verify that signup rejects passwords that do not match.
    # ============================================================

    # Initialize the signup page.
    signup_page = SignupPage(page)

    # Navigate to the signup page.
    signup_page.navigate()

    # Enter different passwords.
    signup_page.fill_signup_form(
        "test@example.com",
        "ValidPass123!",
        "DifferentPass123!"
    )

    # Submit the signup form.
    signup_page.submit()

    # Verify that the password mismatch message is displayed.
    expect(
        page.get_by_text(
            "Confirm password does not match the password.",
            exact=True
        )
    ).to_be_visible()


# ============================================================
# REGISTRATION FUNCTIONAL TESTS
# ============================================================


def test_signup_new_email_account(page):
    # ============================================================
    # Verify that a user can register successfully using
    # a new email address.
    # ============================================================

    # Initialize the signup page.
    signup_page = SignupPage(page)

    # Generate a unique email address.
    email = generate_test_email()

    # Navigate to the signup page.
    signup_page.navigate()

    # Fill in the signup form.
    signup_page.fill_signup_form(
        email,
        TEST_PASSWORD,
        TEST_PASSWORD
    )

    # ============================================================
    # Submit the registration request.
    # ============================================================


def test_signup_new_email_account(page):
    # ============================================================
    # Verify that a user can register successfully using
    # a new email address.
    # ============================================================

    # Initialize the signup page.
    signup_page = SignupPage(page)

    # Generate a unique email address.
    email = generate_test_email()

    # Navigate to the signup page.
    signup_page.navigate()

    # Fill in the signup form.
    signup_page.fill_signup_form(
        email,
        TEST_PASSWORD,
        TEST_PASSWORD
    )

    # ============================================================
    # Submit the registration request.
    # ============================================================

    # Capture the registration API response.
    with page.expect_response(
        lambda response: (
            response.request.method == "POST"
            and "/api/ai_dashboard/create_user" in response.url
        ),
        timeout=15000
    ) as response_info:

        signup_page.submit()

    response = response_info.value
    response_data = response.json()

    # Verify that the registration request succeeded.
    assert response.status == 200, (
        f"Registration request failed. "
        f"HTTP status: {response.status}"
    )

    # Verify that the registered username matches the expected username.
    expected_username = f"ai_dashboard_{email}"

    assert response_data["username"] == expected_username, (
        "Registered username does not match the expected username."
    )

    # ============================================================
    # Verify redirection to the login page.
    # ============================================================

    # Verify that the Sign in button is displayed.
    expect(
        page.get_by_role("button", name="Sign in")
    ).to_be_visible(timeout=15000)

    # Verify that the user is redirected to the login page.
    expect(page).to_have_url(
        "https://dev.app.agnoshealth.com/ai_dashboard/login"
    )



def test_signup_existing_email_rejected(page):
    # ============================================================
    # Verify that an existing email cannot be registered again.
    # ============================================================

    # Initialize the signup page.
    signup_page = SignupPage(page)

    # Navigate to the signup page.
    signup_page.navigate()

    # Fill in the signup form using an existing email.
    signup_page.fill_signup_form(
        EXISTING_EMAIL,
        TEST_PASSWORD,
        TEST_PASSWORD
    )

    # Submit the signup form.
    signup_page.submit()

    # ============================================================
    # Verify that duplicate registration is rejected.
    # ============================================================

    # Verify that the duplicate-email error is displayed.
    expect(
        page.get_by_text(
            "Email already exists",
            exact=False
        )
    ).to_be_visible(timeout=10000)

    # Verify that the success message is not displayed.
    expect(
        page.get_by_text(
            "Your account has been created",
            exact=False
        )
    ).not_to_be_visible()