import os
import time
import json
import requests
from urllib.parse import urljoin, urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class VideoScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited_urls = set()
        self.output_dir = "../downloaded_python_videos"

        # 🔥 Chrome sozlamalari
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--remote-debugging-port=9222")

        # 🔥 Performance log'ni faollashtirish
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        os.makedirs(self.output_dir, exist_ok=True)

    def download_video(self, video_url):
        try:
            video_name = os.path.basename(urlparse(video_url).path)
            file_path = os.path.join(self.output_dir, video_name)

            if os.path.exists(file_path):
                print(f"✅ {video_name} allaqachon yuklab olingan.")
                return

            print(f"⬇️ Yuklanmoqda: {video_url}")
            response = requests.get(video_url, stream=True)

            if response.status_code == 200:
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)
                print(f"✅ Yuklandi: {file_path}")
            else:
                print(f"❌ Yuklab olishda xatolik: {video_url} | Status: {response.status_code}")

        except Exception as e:
            print(f"❌ Yuklab olishda xatolik: {e}")

    def is_python_related(self, text):
        keywords = ["python", "django", "flask", "fastapi", "tensorflow", "pytorch"]
        text = text.lower()
        return any(keyword in text for keyword in keywords)

    def extract_blob_urls(self):
        try:
            logs = self.driver.get_log('performance')  # ✅ Endi ishlaydi!
            for log in logs:
                log_data = json.loads(log["message"])["message"]
                if log_data["method"] == "Network.responseReceived":
                    url = log_data.get("params", {}).get("response", {}).get("url", "")
                    if "blob:" in url:
                        print(f"🚀 Blob URL topildi: {url}")
                        if self.is_python_related(url):
                            self.download_video(url)

        except Exception as e:
            print(f"⚠️ Blob URL olishda xatolik: {e}")

    def scrape_page(self, url):
        if url in self.visited_urls:
            return
        self.visited_urls.add(url)

        print(f"🔎 Tekshirilmoqda: {url}")
        self.driver.get(url)
        time.sleep(3)  # Dinamik yuklanish uchun kutish

        # 🎯 1. Performance log orqali blob URL'larni olish
        self.extract_blob_urls()

        # 🎯 2. Sahifadagi oddiy video fayllarni olish
        soup = self.driver.page_source
        videos = self.driver.find_elements(By.TAG_NAME, "video")
        for video in videos:
            video_url = video.get_attribute("src")
            if video_url and self.is_python_related(video_url):
                self.download_video(video_url)

        sources = self.driver.find_elements(By.TAG_NAME, "source")
        for source in sources:
            video_url = source.get_attribute("src")
            if video_url and self.is_python_related(video_url):
                self.download_video(video_url)

        # 🎯 3. IFRAME ichidagi videolarni olish
        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        for iframe in iframes:
            try:
                src = iframe.get_attribute("src")
                if src and self.is_python_related(src):
                    print(f"🔎 Iframe topildi: {src}")
                    self.driver.get(src)
                    time.sleep(3)
                    self.extract_blob_urls()
            except Exception as e:
                print(f"❌ Iframe olishda xatolik: {e}")

        # 🎯 4. Rekursiv ichki sahifalarni ko‘rib chiqish
        links = self.driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            next_url = link.get_attribute("href")
            link_text = link.text.lower()
            if next_url and self.base_url in next_url and self.is_python_related(link_text):
                self.scrape_page(next_url)

    def start(self):
        try:
            self.scrape_page(self.base_url)
        finally:
            self.driver.quit()
            print("✅✅✅ Barcha Python bilan bog'liq videolar yuklab olindi!")

# 🚀 URLni kiritish
if __name__ == "__main__":
    BASE_URL = "https://42.uz"  # MOHIRDEV saytini tekshirish
    scraper = VideoScraper(BASE_URL)
    scraper.start()