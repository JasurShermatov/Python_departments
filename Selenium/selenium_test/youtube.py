import os
import yt_dlp


class YouTubeDownloader:
    def __init__(self, url):
        self.url = url
        self.output_dir = "downloaded_videos"
        os.makedirs(self.output_dir, exist_ok=True)

    def download_video(self):
        ydl_opts = {
            # 🔥 Eng yuqori sifatdagi videoni yuklab oladi
            "format": "bestvideo+bestaudio/best",
            # ✅ Fayl nomini tartib bilan saqlaydi
            "outtmpl": f"{self.output_dir}/%(title)s.%(ext)s",
            # 🚀 Parallel yuklashni faollashtirish
            "concurrent_fragment_downloads": 5,
            # ⚡️ Yuklab olish tezligini oshirish
            "n_threads": 4,
            "noplaylist": False,  # Playlist ichidagi barcha videolarni yuklab oladi
            "ignoreerrors": True,  # Xatolarni e’tiborsiz qoldiradi
            # 🔐 Agar kirish cheklangan bo‘lsa, cookies ishlatish mumkin
            # 'cookiefile': 'cookies.txt',
            "merge_output_format": "mp4",  # MP4 formatida saqlaydi
            "progress_hooks": [self.progress_hook],
            # 🔇 Loglarni o‘chiradi
            "quiet": False,
            "no_warnings": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])

    def progress_hook(self, d):
        if d["status"] == "finished":
            print(f"✅ Yuklab olindi: {d['filename']}")
        elif d["status"] == "downloading":
            percent = d.get("_percent_str", "0%")
            speed = d.get("_speed_str", "0 MB/s")
            eta = d.get("_eta_str", "--")
            print(f"⬇️ Yuklanmoqda: {percent} | {speed} | ETA: {eta}")


if __name__ == "__main__":
    URL = "https://www.youtube.com/watch?v=SJIRB6GkKcM&t=2253s&pp=ygUTc2hheHpvZGJlayBNdXh0b3JvdtIHCQm9AIO1pN6f1A%3D%3D"
    downloader = YouTubeDownloader(URL)
    downloader.download_video()
