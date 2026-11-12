
from playwright.sync_api import Page
from datetime import datetime


class DashboardPage:

    def __init__(self, page: Page):
        self.page = page

        # ====================================================
        # NAVIGATION
        # ====================================================

        self.diagnosis_list_button = page.get_by_role(
            "button", name="Diagnosis List"
        )

        self.logout_button = page.get_by_role(
            "button", name="Log Out"
        )

        # ====================================================
        # DOWNLOAD
        # ====================================================

        self.download_button = page.get_by_role(
            "button",
            name="download Download",
            exact=True
        )

        self.channel_download_button = page.get_by_role(
            "button",
            name="Channel download",
            exact=True
        )

        self.download_confirmation_title = page.get_by_text(
            "ยินยันการดาวน์โหลด",
            exact=True
        )

        self.confirm_download_button = page.get_by_role(
            "link",
            name="ยืนยัน",
            exact=True
        )

        # ====================================================
        # SEARCH
        # ====================================================

        self.search_input = page.get_by_role(
            "textbox",
            name="Patient name, Patient contact, Record ID, Record code"
        )

        self.search_button = page.get_by_role(
            "button",
            name="Search",
            exact=True
        )

        # ====================================================
        # STATUS FILTERS
        # ====================================================

        self.completed_filter = page.get_by_text(
            "Completed", exact=True
        )

        self.open_filter = page.get_by_text(
            "Open", exact=True
        )

        self.in_progress_filter = page.get_by_text(
            "In progress", exact=True
        )

        # ====================================================
        # TRIAGE FILTERS
        # ====================================================

        self.all_triage_filter = page.get_by_text(
            "All", exact=True
        )

        self.self_care_filter = page.get_by_text(
            "Self care", exact=True
        )

        self.seek_medical_filter = page.get_by_text(
            "Seek Medical", exact=True
        )

        self.urgent_filter = page.get_by_text(
            "Urgent", exact=True
        )

        self.emergency_filter = page.get_by_text(
            "Emergency", exact=True
        )

        # ====================================================
        # DASHBOARD RESULTS
        # ====================================================

        self.total_cases = page.get_by_text(
            "Total cases : 1", exact=True
        )

        self.total_cases_label = page.get_by_text(
            "Total cases :", exact=False
        )

        self.empty_diagnosis_message = page.get_by_text(
            "ยังไม่มีข้อมูลการวินิจฉัย",
            exact=True
        )

        # ====================================================
        # CHANNEL FILTER
        # ====================================================

        self.channel_dropdown = page.locator(
            "button.css-1bmkooo"
        )

        # ====================================================
        # DATE FILTER
        # ====================================================

        self.date_picker = page.get_by_text(
            "Select date",
            exact=True
        )

        self.date_menu_today = page.get_by_text(
            "Today",
            exact=True
        )

    # ========================================================
    # NAVIGATION METHODS
    # ========================================================

    def open_diagnosis_list(self):
        self.diagnosis_list_button.click()

    def logout(self):
        self.logout_button.click()

    # ========================================================
    # DOWNLOAD METHODS
    # ========================================================

    def click_download(self):
        self.download_button.click()

    def confirm_download(self):
        self.confirm_download_button.click()

    def click_channel_download(self):
        self.channel_download_button.click()

    # ========================================================
    # SEARCH METHODS
    # ========================================================

    def search(self, keyword):
        self.search_input.fill(keyword)
        self.search_button.click()

    # ========================================================
    # STATUS FILTER METHODS
    # ========================================================

    def select_completed_filter(self):
        self.completed_filter.click()

    def select_open_filter(self):
        self.open_filter.click()

    def select_in_progress_filter(self):
        self.in_progress_filter.click()

    # ========================================================
    # TRIAGE FILTER METHODS
    # ========================================================

    def select_all_triage_filter(self):
        self.all_triage_filter.click()

    def select_self_care_filter(self):
        self.self_care_filter.click()

    def select_seek_medical_filter(self):
        self.seek_medical_filter.click()

    def select_urgent_filter(self):
        self.urgent_filter.click()

    def select_emergency_filter(self):
        self.emergency_filter.click()

        # ========================================================
    # CHANNEL FILTER METHODS
    # ========================================================

    def open_channel_dropdown(self):
        self.channel_dropdown.click()

    def get_channel_option(self, channel_name):
        return self.channel_dropdown.locator(
            "div.css-l57wbg > div"
        ).filter(
            has_text=channel_name
        )

    def select_channel_option(self, channel_name):
        self.get_channel_option(channel_name).click()

    def is_channel_selected(self, channel_name):
        option_row = self.get_channel_option(channel_name)

        checkbox_image = option_row.locator("img")

        image_src = checkbox_image.get_attribute("src")

        return (
            image_src is not None
            and "checkbox-check-fill-blue" in image_src
        )

    # ============================================================
    # DATE FILTER TEST
    # ============================================================

    def open_date_calendar(self):
        # Open the date filter.
        self.date_picker.click()

    def select_today_date(self):
        # Select Today from the date menu.
        self.date_menu_today.click()

    def test_date_calendar_selection(page):
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)

        login_page.navigate()
        login_page.login("test@gmail.com", "12345")

        expect(dashboard_page.diagnosis_list_button).to_be_visible()

        # Open date filter.
        dashboard_page.open_date_calendar()

        # Verify Today option is visible.
        expect(dashboard_page.date_menu_today).to_be_visible()

        # Select Today.
        dashboard_page.select_today_date()

        # Verify selected date is displayed.
        expect(
            page.get_by_text("Select date", exact=True)
        ).not_to_be_visible()

        expect(
            page.get_by_text("Today", exact=True)
        ).to_be_visible()