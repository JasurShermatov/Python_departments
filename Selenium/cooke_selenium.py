# bu yerda session id orqali instagramga kirsa boladi yaniy
# application ichiga cookes ichiga session_id ni olish kerak
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 30)

instagram_session_id=os.getenv("INSTAGRAM_SESSION_ID")


try:
    driver.get("https://www.instagram.com")
    driver.add_cookie({"name": "sessionid", "value": "19545839310%3AQZ8a493YovI4td%3A15%3AAYfmHpFN7DlRsk5Xyqids2VNN9vHWCwOgkdukMoWBA"})
    driver.refresh()
    time.sleep(100)
except Exception as e:
    driver.save_screenshot("screenshot.png")
    print(f"An error occurred: {e}")