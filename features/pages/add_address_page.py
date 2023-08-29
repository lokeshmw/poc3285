from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class Add_address(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_xpath = "//a[contains(.,'Hello, Lokesh.M')]"
    click_address_xpath = "//h2[normalize-space()='Your Addresses']"
    click_add_address_id = "ya-myab-plus-address-icon"
    enter_name_xpath = "//input[@id='address-ui-widgets-enterAddressFullName']"
    enter_num_xpath = "//input[@id='address-ui-widgets-enterAddressPhoneNumber']"
    enter_pin_xpath = "//input[@id='address-ui-widgets-enterAddressPostalCode']"
    enter_address1_xpath = "//input[@id='address-ui-widgets-enterAddressLine1']"
    enter_address2_xpath = "//input[@id='address-ui-widgets-enterAddressLine2']"
    click_add_address_xpath = "//input[@aria-labelledby='address-ui-widgets-form-submit-button-announce']"
    add_address_text_xpath = "//h4[@class='a-alert-heading']"

    def click_account(self):
        self.click_on_element("account_xpath", self.account_xpath)

    def click_address(self):
        self.click_on_element("click_address_xpath", self.click_address_xpath)

    def click_add_address(self):
        self.click_on_element("click_add_address_id", self.click_add_address_id)

    def enter_name(self, a):
        self.type_into_element("enter_name_xpath", self.enter_name_xpath, a)

    def enter_num(self, a):
        self.type_into_element("enter_num_xpath", self.enter_num_xpath, a)

    def enter_pin(self, a):
        self.type_into_element("enter_pin_xpath", self.enter_pin_xpath, a)

    def enter_address1(self, a):
        self.type_into_element("enter_address1_xpath", self.enter_address1_xpath, a)

    def enter_address2(self, a):
        self.type_into_element("enter_address2_xpath", self.enter_address2_xpath, a)

    def click_Add_address(self):
        self.click_on_element("click_add_address_xpath", self.click_add_address_xpath)

    def verify_text(self, a):
        return self.contains("add_address_text_xpath", self.add_address_text_xpath, a)
