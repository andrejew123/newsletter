import page_objects.base as base
from lookups.locator import Locator


class SubscriptionPage(base.BasePage):
    """
    Buttons and methods used on Search Page
    """

    def __init__(self, driver):
        super().__init__(driver)

        self.newsletter_email = Locator(
            driver=self.driver,
            selector="#newsletter_email"
        )
        self.dropdown_menu = Locator(
            driver=self.driver,
            selector=".ant-select-selection__placeholder"
        )
        self.start_date = Locator(
            driver=self.driver,
            selector="#newsletter_startDate .ant-calendar-picker-input"
        )
        self.end_date = Locator(
            driver=self.driver,
            selector="#newsletter_endDate .ant-calendar-picker-input"
        )
        self.error_notification = Locator(
            driver=self.driver,
            selector=".ant-notification-notice-description"
        )
        self.agreement_checkbox = Locator(
            driver=self.driver,
            selector=".ant-checkbox"
        )
        self.submit_button = Locator(
            driver=self.driver,
            selector="button"
        )
        self.confirmation_modal = Locator(
            driver=self.driver,
            selector=".ant-modal-confirm-title"
        )
        self.empty_fields = Locator(
            driver=self.driver,
            selector=".ant-form-explain",
            many=True
        )
        self.agreement_link = Locator(
            driver=self.driver,
            selector="//a[contains(text(), 'agreement')]",
            by="xpath"
        )
        self.agreement_title = Locator(
            driver=self.driver,
            selector=".DP1T8c"
        )
        self.ok_button = Locator(
            driver=self.driver,
            selector="//span[text() = 'OK']/parent::button",
            by="xpath"
        )
        self.email_already_in_use_warning = Locator(
            driver=self.driver,
            selector="#warning"
        )

    def get_data(self, data):
        return Locator(
            driver=self.driver,
            selector="#newsletter_{}".format(data),
        )

    def select_from_dropdown_menu(self, newsletter_type):
        return Locator(
            driver=self.driver,
            selector="//*[text()='{}']".format(newsletter_type),
            by="xpath",
        )

    def choosing_today_date(self, date):
        return Locator(
            driver=self.driver,
            selector="[title='{}']".format(date),
            many=True,
        )

    def choosing_today_date(self, date):
        return Locator(
            driver=self.driver,
            selector="[title='{}']".format(date),
            many=True,
        )
