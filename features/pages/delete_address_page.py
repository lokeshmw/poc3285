import time

from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class Delete_address(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_xpath = "//a[contains(.,'Hello, Lokesh.M')]"
    click_address_xpath = "//h2[normalize-space()='Your Addresses']"
    all_address_xpath = "//div[@class ='a-row a-spacing-micro']/div/div"
    address_name_xpath = "//div[@class ='a-row a-spacing-micro']/div/div/div/div/div/ul/li[1]"
    remove_address_xpath = "//div[@class ='a-row a-spacing-micro']/div/div/span/a[text()='Remove']"
    yes_delete_xpath = "//div[@class ='a-popover-inner']/div[@class='a-section']/div[4]/div[2]/div/div[@class='a-column a-span8']"
    deleted_text_xpath = "//h4[.='Address deleted']"

    def click_account(self):
        self.click_on_element("account_xpath", self.account_xpath)

    def click_address(self):
        self.click_on_element("click_address_xpath", self.click_address_xpath)

    def delete_address(self):
        addresses = self.driver.find_elements(By.XPATH, "//div[@class ='a-row a-spacing-micro']/div/div")
        for x in addresses:
            address_name = x.find_element(By.XPATH, "div/div/div/ul/li[1]")
            print(address_name)
            if address_name.text == "Lokesh.M":
                x.driver.find_element(By.XPATH, "span/a[text()='Remove']").click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, "//div[@class ='a-popover-inner']/div[@class='a-section']/div[4]/div[2]/div/div[@class='a-column a-span8']").click()

    def verify_text(self):
        return self.text_equal("deleted_text_xpath", self.deleted_text_xpath, "Address deleted")
