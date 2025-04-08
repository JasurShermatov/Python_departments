import os
import psutil
import time
import threading
import numpy as np
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor


def cpu_intensive_task():
    """CPU ni maksimal darajada ishlatadigan funksiya"""
    start_time = time.time()
    # 10 soniya davomida CPU ni maksimal ishlatish
    while time.time() - start_time < 10:
        # Katta matritsa ko'paytirish - CPU uchun og'ir operatsiya
        matrix_size = 1000
        matrix_a = np.random.rand(matrix_size, matrix_size)
        matrix_b = np.random.rand(matrix_size, matrix_size)
        result = np.dot(matrix_a, matrix_b)
    return "CPU testi tugadi"


def memory_intensive_task():
    """Xotirani maksimal darajada ishlatadigan funksiya"""
    # Xotirangizga qarab, bu raqamni o'zgartiring
    # Ehtiyot bo'ling, juda katta son qo'yish tizimingizni sekinlashtirib qo'yishi mumkin
    try:
        # 1 GB xotirani band qilish (tizimlarga qarab o'zgartiring)
        memory_size = 1024 * 1024 * 1024  # 1 GB
        data = bytearray(memory_size)  # Xotirani band qilish
        time.sleep(5)  # 5 soniya ushlab turish
    except MemoryError:
        print("Xotira yetishmadi - kichikroq qiymat bilan qayta urinib ko'ring")
    return "Xotira testi tugadi"


def monitor_system(duration=15):
    """Tizim resurslarini kuzatish"""
    cpu_usage = []
    memory_usage = []
    timestamps = []

    start_time = time.time()
    while time.time() - start_time < duration:
        cpu_percent = psutil.cpu_percent(interval=0.5)
        memory_percent = psutil.virtual_memory().percent

        cpu_usage.append(cpu_percent)
        memory_usage.append(memory_percent)
        timestamps.append(time.time() - start_time)

        print(f"Vaqt: {time.time() - start_time:.1f}s | CPU: {cpu_percent}% | Xotira: {memory_percent}%")

    return timestamps, cpu_usage, memory_usage


def plot_results(timestamps, cpu_usage, memory_usage):
    """Natijalarni grafikda ko'rsatish"""
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, cpu_usage, label='CPU foydalanish %')
    plt.plot(timestamps, memory_usage, label='Xotira foydalanish %')
    plt.xlabel('Vaqt (soniya)')
    plt.ylabel('Foydalanish foizi')
    plt.title('Tizim resurslari foydalanish darajasi')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('system_performance.png')
    plt.show()


def main():
    print("Kompyuter kuchliligini tekshirish uchun test boshlanmoqda...")
    print(f"CPU yadrolar soni: {os.cpu_count()}")
    print(f"Jami xotira: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")

    # Monitoring jarayonini alohida oqimda boshlash
    monitor_thread = threading.Thread(target=lambda: monitor_system(20))
    monitor_thread.start()

    # CPU va xotira testlarini parallel ravishda ishga tushirish
    time.sleep(2)  # Monitoring boshlanishi uchun kutish
    print("\nTestlar boshlanmoqda...")

    with ThreadPoolExecutor() as executor:
        cpu_future = executor.submit(cpu_intensive_task)
        memory_future = executor.submit(memory_intensive_task)

        # Natijalarni kutish
        cpu_result = cpu_future.result()
        memory_result = memory_future.result()

    print(f"\n{cpu_result}")
    print(f"{memory_result}")

    # Monitoring jarayoni tugashini kutish
    monitor_thread.join()

    # Kompyuter haqida qo'shimcha ma'lumotlar
    print("\nKompyuter haqida qo'shimcha ma'lumotlar:")
    print(f"CPU modeli: {psutil.cpu_freq().current:.2f} MHz")
    print(f"CPU maksimal chastotasi: {psutil.cpu_freq().max:.2f} MHz (agar mavjud bo'lsa)")

    disk_usage = psutil.disk_usage('/')
    print(f"Disk hajmi: {disk_usage.total / (1024 ** 3):.2f} GB")
    print(f"Bo'sh disk hajmi: {disk_usage.free / (1024 ** 3):.2f} GB")

    # Natijalarni grafikda ko'rsatish
    try:
        # Monitoring natijalarini olish
        timestamps, cpu_usage, memory_usage = monitor_system(0)  # 0 soniya chunki monitoring allaqachon tugagan
        plot_results(timestamps, cpu_usage, memory_usage)
    except Exception as e:
        print(f"Grafikni chizishda xatolik: {e}")

    print("\nTest muvaffaqiyatli yakunlandi!")


if __name__ == "__main__":
    try:
        # Kerakli modullarni tekshirish
        missing_modules = []
        for module in ["psutil", "numpy", "matplotlib"]:
            try:
                __import__(module)
            except ImportError:
                missing_modules.append(module)

        if missing_modules:
            print(f"Quyidagi modullar o'rnatilmagan: {', '.join(missing_modules)}")
            print("Ularni quyidagi buyruq bilan o'rnatishingiz mumkin:")
            print(f"pip install {' '.join(missing_modules)}")
        else:
            main()
    except KeyboardInterrupt:
        print("\nTest foydalanuvchi tomonidan to'xtatildi.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")