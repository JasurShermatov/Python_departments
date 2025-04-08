import time
from selenium import webdriver

driver = webdriver.Chrome()
try:
    driver.get("https://www.shaxzodbek.com/")
    time.sleep(15)
    driver.back()
    time.sleep(5)
    driver.forward()
    time.sleep(5)
    driver.refresh()
    time.sleep(3)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.close()
