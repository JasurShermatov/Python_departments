import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urljoin, urlparse


class WebsiteScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited_urls = set()
        self.output_dir = "scraped_data"

        # Chrome sozlamalari
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Brauzerni yashirin rejimda ishga tushirish
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # Papkalarni yaratish
        os.makedirs(self.output_dir, exist_ok=True)

    def save_file(self, url, content, sub_dir=""):
        path = urlparse(url).path
        if path.endswith('/'):
            path += 'index.html'
        elif not os.path.splitext(path)[1]:
            path += '.html'

        file_path = os.path.join(self.output_dir, sub_dir, path.lstrip('/'))
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as file:
            file.write(content)

        print(f"✅ Saved: {file_path}")

    def download_static_file(self, url, sub_dir=""):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.save_file(url, response.content, sub_dir=sub_dir)
        except Exception as e:
            print(f"❌ Error downloading {url}: {e}")

    def scrape_page(self, url):
        if url in self.visited_urls:
            return
        self.visited_urls.add(url)

        print(f"🔎 Scraping: {url}")

        # Sahifani ochish
        self.driver.get(url)
        time.sleep(2)  # JavaScript yuklanishini kutish

        # Sahifa tarkibini olish
        soup = BeautifulSoup(self.driver.page_source, "html.parser")

        # Sahifani saqlash
        self.save_file(url, self.driver.page_source.encode("utf-8"))

        # Rasmlar, CSS va JS fayllarni yuklab olish
        for img in soup.find_all("img", src=True):
            src = urljoin(url, img["src"])
            self.download_static_file(src, sub_dir="images")

        for css in soup.find_all("link", href=True):
            href = urljoin(url, css["href"])
            if href.endswith(".css"):
                self.download_static_file(href, sub_dir="css")

        for js in soup.find_all("script", src=True):
            src = urljoin(url, js["src"])
            if src.endswith(".js"):
                self.download_static_file(src, sub_dir="js")

        # Ichki havolalarni topish va qayta ishlash
        for link in soup.find_all("a", href=True):
            next_url = urljoin(url, link["href"])
            if self.base_url in next_url and next_url not in self.visited_urls:
                self.scrape_page(next_url)

    def start(self):
        try:
            self.scrape_page(self.base_url)
        finally:
            self.driver.quit()
            print("✅✅✅ Scraping completed!")


# 🔥 Saytni olish uchun URL kiriting
if __name__ == "__main__":
    BASE_URL = "https://mohirdev.uz"
    scraper = WebsiteScraper(BASE_URL)
    scraper.start()