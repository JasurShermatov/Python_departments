import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.axcapital.ae/buy/dubai/properties-for-sale")
time.sleep(5)

property_cards = driver.find_elements("class name", "property-card")
for i in range(len(property_cards)):
    try:
        property_cards[i].click()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        property_cards = driver.find_elements(
            "class name", "property-card"
        )  # Refresh the list
    except Exception as e:
        print(f"Error card {i}: {e}")
        driver.execute_script("window.scrollBy(0, 300);")  # Scroll down
        time.sleep(2)
        property_cards = driver.find_elements(
            "class name", "property-card"
        )  # Refresh the list
