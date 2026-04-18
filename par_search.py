#vonmarie
# Parallel Linear Search

from multiprocessing import Process, Queue

def worker(sub_data, target, q, offset):
    for i, val in enumerate(sub_data):
        if val == target:
            q.put(offset + i)
            return
    q.put(-1)


def parallel_search(data, target):
    processes = []
    q = Queue()
    chunk_size = len(data) // 4

    for i in range(4):
        start = i * chunk_size
        end = len(data) if i == 3 else (i + 1) * chunk_size

        p = Process(target=worker, args=(data[start:end], target, q, start))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    while not q.empty():
        result = q.get()
        if result != -1:
            return result

    return -1