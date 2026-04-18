#Jorgie
# Parallel Merge Sort

from multiprocessing import Pool
from seq_sort import sequential_merge_sort, merge

def parallel_merge_sort(arr):
    if len(arr) <= 1000:
        return sequential_merge_sort(arr)

    mid = len(arr) // 2

    with Pool(2) as pool:
        left, right = pool.map(sequential_merge_sort, [arr[:mid], arr[mid:]])

    return merge(left, right)