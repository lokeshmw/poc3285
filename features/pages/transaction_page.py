from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class transaction_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    account_xpath = "//a[contains(.,'Hello, Lokesh.M')]"
    amazon_pay_xpath = "//h2[normalize-space()='Amazon Pay balance']"
    amazon_symbol_xpath = "//img[@alt='AmazonPay Dashboard Link']"
    transaction_xpath = "//a[@href='/pay/history?ref_=apay_deskhome_ViewStatement']//div[@class='a-section a-spacing-small a-text-center']//img"
    all_transactions_xpath = "//div[@class='a-section celwidget']/span/div/a/span/div/div/div[2]/div/"
    transaction_name_xpath = "div/div[@class='a-section pad-header-text']"
    amount_xpath = "div[2]"

    def click_account(self):
        self.click_on_element("account_xpath", self.account_xpath)

    def click_amazon_pay(self):
        self.click_on_element("amazon_pay_xpath", self.amazon_pay_xpath)

    def click_amazon_symbol(self):
        self.click_on_element("amazon_symbol_xpath", self.amazon_symbol_xpath)

    def click_transaction_xpath(self):
        self.click_on_element("transaction_xpath", self.transaction_xpath)

    def print_transactions(self):

        transactions = self.driver.find_elements(By.XPATH, "//DIV[@class='a-section celwidget']/span/div/a/span/div/div/div[2]/div")
        a = []
        for x in transactions:
            transaction_name = x.find_element(By.XPATH, "div/div[@class='a-section pad-header-text']").text
            transaction_amount = x.find_element(By.XPATH, "div[2]").text
            b = [transaction_name, transaction_amount]
            a.append(b)
        return a
