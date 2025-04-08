from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time



options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920x1080")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.page_load_strategy = "eager"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.axcapital.ae/")

wait = WebDriverWait(driver, 10)


last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break
    last_height = new_height


people = driver.find_elements(By.CLASS_NAME, "content_info-inner")

all_names = []
for person in people:
    try:
        name = person.find_element(By.TAG_NAME, "a").text.strip()
        if name and name not in all_names:
            all_names.append(name)
    except:
        continue


print("Barcha ismlar:")
for idx, name in enumerate(all_names, start=1):
    print(f"{idx}- {name}")

driver.quit()