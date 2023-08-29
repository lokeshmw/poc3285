import time

from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class Change_address(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_xpath = "//a[contains(.,'Hello, Lokesh.M')]"
    click_address_xpath = "//span[@id='glow-ingress-line2']"
    all_address_xpath = "//ul[@class='a-nostyle a-button-list a-declarative a-button-toggle-group a-vertical']/li"

    def click_account(self):
        self.click_on_element("account_xpath", self.account_xpath)

    def click_address(self):
        self.click_on_element("click_address_xpath", self.click_address_xpath)

    def change_address(self):
        addresses = self.driver.find_elements(By.XPATH, self.all_address_xpath)
        print(addresses)
        for i in addresses:
            print(i.text)
            if i.text.startswith("Lokesh.M"):
                i.click()


