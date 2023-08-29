import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/ref=nav_logo")
time.sleep(20)
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@data-csa-c-content-id='nav_ya_signin']").click()
driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys(8105000676)
driver.implicitly_wait(10)
driver.find_element(By.ID, 'continue').click()
driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("Loki@1234")
driver.find_element(By.ID, "auth-signin-button").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Cart']").click()
cart_items = driver.find_elements(By.XPATH, "//form[@id='activeCartViewForm']/div[@data-name='Active Items']/div")
for i in cart_items:
    name = i.find_element(By.XPATH, "div[@class='sc-list-item-content']/div/div[@class='sc-item-content-group']/ul/li/span/a/span/span")
    print(name.text)
