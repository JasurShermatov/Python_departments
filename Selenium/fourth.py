import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get('https://www.axcapital.ae/')

l = driver.find_element(By.XPATH, '//input[@placeholder="Your name"]')

driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: });", l)

time.sleep(8)
l.click()

l.send_keys("John")

time.sleep(10)
