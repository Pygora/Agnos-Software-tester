# Agnos Health AI Dashboard - Automated Testing

Automated web application testing for the Agnos Health AI Dashboard using **Python, Playwright, and Pytest**.

This project uses the Page Object Model (POM) design pattern to organize page elements and actions separately from test cases, making the test suite easier to maintain and extend.

## Tech Stack

- **Python** - Programming language
- **Playwright** - Browser automation
- **Pytest** - Test framework
- **python-dotenv** - Environment variable management

## Project Structure

agnosd-web-tests/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── signup_page.py
│   └── dashboard_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_signup.py
│   ├── test_filter.py
│   ├── test_search.py
│   └── test_download.py
│
├── .env
├── .gitignore
├── config.py
├── pytest.ini
├── requirements.txt
└── README.md

## Test Coverage

### 1. Login
- Verify that the login page accepts valid credentials.
- Verify that login is rejected with an incorrect password.
- Verify that the Sign In button is disabled when the fields are empty.

### 2. Logout
- Verify that users can log out successfully.
- Verify that logged-out users cannot access the dashboard directly.

### 3. Signup
- Verify that the signup page loads correctly.
- Verify that the Confirm button is disabled when all fields are empty.
- Verify email format validation.
- Verify password requirements.
- Verify password confirmation matching.
- Verify successful registration using a new email address.
- Verify that duplicate email registration is rejected.

### 4. Filters
- Verify default status and triage filter options.
- Verify channel filter default selections.
- Verify channel filter selection and deselection.
- Verify date calendar selection.

### 5. Search
- Verify that searching for a keyword with no matching records displays the empty state.

### 6. Download
- Verify that the diagnosis list generates a Blob download URL after confirming the download.

## Prerequisites

- Python 3.10 or later
- Google Chrome or another supported Playwright browser
- Git



## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd agnosd-web-tests
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows PowerShell**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install chromium
```

### 5. Configure environment variables

Create a `.env` file in the project root.

```env
BASE_URL=https://dev.app.agnoshealth.com

TEST_EMAIL = test_email@example.com
TEST_PASSWORD = login_password
SIGNUP_TEST_PASSWORD = signup_password
INVALID_LOGIN_PASSWORD = invalid_password

TEST_STATUS_FILTERS = Open,In progress,Completed
TEST_TRIAGE_FILTERS = All,Self care,Seek Medical,Urgent,Emergency
TEST_CHANNEL_FILTERS = All,Agnos application,Vimut hospital,Vimut telemed,Siam smile
TEST_INDIVIDUAL_CHANNELS = Agnos application,Vimut hospital,Vimut telemed,Siam smile
TEST_DATE_FILTER = Today
```

Replace the example credentials with authorized test account credentials.

**Important:** Do not commit `.env` file or expose test account credentials in a public repository.

## Running Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_login.py
```

```bash
pytest tests/test_signup.py
```

```bash
pytest tests/test_filter.py
```

Run a specific test:

```bash
pytest tests/test_login.py::test_login_success
```

Run tests with detailed output:

```bash
pytest -v -s
```

## Test Design

This project follows the **Page Object Model (POM)** pattern.

- `pages/` contains page classes, locators, and reusable interactions.
- `tests/` contains test scenarios and assertions.
- `config.py` loads environment-specific settings and test data.
- `.env` stores local configuration and credentials.
- `pytest.ini` defines Pytest discovery settings.

This separation helps reduce duplicated code and makes it easier to update locators when the application changes.

## Notes

- Tests are designed for the Agnos Health AI Dashboard development environment.
- Valid login credentials are required for authenticated test scenarios.
- Signup tests generate unique email addresses for new registration attempts.
- Some test scenarios depend on the application's current UI behavior and test data.
- The download test currently verifies Blob URL generation, not the contents of a downloaded CSV file.
