import multiprocessing
import time

def read_file_part(file_path, start, end):
    with open(file_path, "rb") as f:
        f.seek(start)
        return f.read(end - start)

if __name__ == "__main__":
    file_path = "bigfile.dat"

    file_size = 10_000_000_000
    num_cores = multiprocessing.cpu_count()
    chunk_size = file_size // num_cores

    start_time = time.time()

    with multiprocessing.Pool(num_cores) as pool:
        results = pool.starmap(read_file_part, [(file_path, i * chunk_size, (i + 1) * chunk_size) for i in range(num_cores)])

    print(f"Barcha faylni o‘qish vaqti: {time.time() - start_time:.2f} soniya")