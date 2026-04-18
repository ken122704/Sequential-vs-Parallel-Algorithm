#ken
#main
import time
from dataset import generate_data, generate_sorted_data, generate_reverse_sorted_data
from seq_sort import sequential_merge_sort
from par_sort import parallel_merge_sort
from seq_search import linear_search
from par_search import parallel_search


def test_all(n):
    print(f"\n--- Testing with {n} elements ---")

    data = generate_data(n)
    target = data[-1]

    # Sequential Sort
    start = time.time()
    sequential_merge_sort(data.copy())
    print("Sequential Sort Time:", time.time() - start)

    # Parallel Sort
    start = time.time()
    parallel_merge_sort(data.copy())
    print("Parallel Sort Time:", time.time() - start)

    # Sequential Search
    start = time.time()
    linear_search(data, target)
    print("Sequential Search Time:", time.time() - start)

    # Parallel Search
    start = time.time()
    parallel_search(data, target)
    print("Parallel Search Time:", time.time() - start)


def test_special_cases(n):
    print(f"\n--- Special Case (Sorted) {n} ---")
    data = generate_sorted_data(n)
    target = data[-1]

    print("Sequential Search:", linear_search(data, target))
    print("Parallel Search:", parallel_search(data, target))

    print(f"\n--- Special Case (Reverse Sorted) {n} ---")
    data = generate_reverse_sorted_data(n)
    target = data[-1]

    print("Sequential Search:", linear_search(data, target))
    print("Parallel Search:", parallel_search(data, target))


if _name_ == "_main_":
    test_all(1000)
    test_all(100000)
    test_all(1000000)

    test_special_cases(1000)