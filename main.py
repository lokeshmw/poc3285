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
driver.find_element(By.XPATH, "//a[contains(.,'Hello, Lokesh.M')]").click()
driver.find_element(By.XPATH, "//h2[normalize-space()='Your Addresses']").click()
addresses = driver.find_elements(By.XPATH, "//div[@class ='a-row a-spacing-micro']/div/div")
for x in addresses:
    phone_name = driver.find_element(By.XPATH, "//div[@class ='a-row a-spacing-micro']/div/div/div/div/div/ul/li[1]")
    if phone_name.text == "Lokesh.M":
        driver.find_element(By.XPATH, "//div[@class ='a-row a-spacing-micro']/div/div/span/a[text()='Remove']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@class ='a-popover-inner']/div[@class='a-section']/div[4]/div[2]/div/div[@class='a-column a-span8']").click()
        time.sleep(10)
        print(driver.find_element(By.XPATH, "//h4[.='Address deleted']").text)

        # // div[ @
        #
        #
        # //div [@class ='a-row a-spacing-micro']/div/div/div/div/div/ul/li[1]
        # // div[@ class ='a-row a-spacing-micro'] / div / div / span / a[text()="Remove"]
