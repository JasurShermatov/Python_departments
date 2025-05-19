import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(BASE_DIR, "downloads"), exist_ok=True)
print(BASE_DIR)

options = webdriver.ChromeOptions()


options.add_experimental_option(
    "prefs",
    {"download.default_directory": os.path.join(BASE_DIR, "downloads")},
)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

driver.get("https://www.shaxzodbek.com")

time.sleep(2)

driver.find_element("xpath", "/html/body/main/section[1]/div/div[2]/a[5]").click()

time.sleep(2)
