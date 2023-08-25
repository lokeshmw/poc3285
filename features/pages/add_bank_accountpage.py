import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.pages.BasePage import BasePage


class add_Bank_AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_xpath = "//a[contains(.,'Hello, Lokesh.M')]"
    payment_options_xpath = "//div[@data-card-identifier='PaymentOptions']"
    manage_account_xpath = "//div[contains(text(),'Manage Bank Accounts')]"
    add_new_account_xpath = "//span[@class='a-size-base']"
    ifsc_yes_button_xpath = "//span[normalize-space()='Yes']"
    enter_ifsc_xpath = "//input[@id='enterIFSCInput']"
    confirm_ifsc_xpath = "//span[contains(text(),'Confirm IFSC')]"
    enter_holder_name_xpath = "//input[@id='addBankAccountHolderName']"
    enter_accountNo_xpath = "//input[@id='addBankAccountNumber']"
    enter_confirm_accountNo_xpath = "//input[@id='confirmAddBankAccountNumber']"
    symbol_xpath = "//i[@class='a-icon a-icon-dropdown']"
    savings_click_xpath = "//a[@id='addBankAccountType_2']"
    account_type_xpath = "//select[@id='addBankAccountType']"
    savings_xpath = "//a[@data-value='{'stringVal':'savings'}']"
    save_account_xpath = "//button[@id='saveWithoutValidationButton']"
    account_added_text_xpath = "//span[@class='a-size-large a-color-success']"

    def click_on_account(self):
        self.click_on_element("account_xpath", self.account_xpath)

    def click_payment_options(self):
        self.click_on_element("payment_options_xpath", self.payment_options_xpath)

    def click_manage_account(self):
        self.click_on_element("manage_account_xpath", self.manage_account_xpath)

    def click_add_new_account(self):
        self.click_on_element("add_new_account_xpath", self.add_new_account_xpath)

    def click_ifsc_yes(self):
        self.click_on_element("ifsc_yes_button_xpath", self.ifsc_yes_button_xpath)

    def enter_ifsc(self, ifsc):
        self.type_into_element("enter_ifsc_xpath", self.enter_ifsc_xpath, ifsc)

    def click_ifsc_confirm(self):
        self.click_on_element("confirm_ifsc_xpath", self.confirm_ifsc_xpath)

    def enter_holder_name(self, name):
        self.type_into_element("enter_holder_name_xpath", self.enter_holder_name_xpath, name)

    def enter_accountNo(self, acc_no):
        self.type_into_element("enter_accountNo_xpath", self.enter_accountNo_xpath, acc_no)

    def enter_confirm_accountNo(self, acc_no):
        self.type_into_element("enter_confirm_accountNo_xpath", self.enter_confirm_accountNo_xpath, acc_no)

    def Account_type(self):
        # self.click_on_element("account_type_xpath", self.account_type_xpath)

        dropdown = Select(self.driver.find_element(By.XPATH, "//select[@id='addBankAccountType']"))
        time.sleep(2)
        dropdown.select_by_visible_text("Savings")
        time.sleep(5)
        self.click_on_element("savings_click_xpath", self.savings_click_xpath)

    def click_save_account(self):
        self.click_on_element("save_account_xpath", self.save_account_xpath)

    def verify_account_added(self, a):
        return self.contains("account_added_text_xpath", self.account_added_text_xpath, a)
