#ken
#dataset
import random

def generate_data(n):
    return [random.randint(1, 1000000) for _ in range(n)]


def generate_sorted_data(n):
    data = generate_data(n)
    return sorted(data)


def generate_reverse_sorted_data(n):
    data = generate_data(n)
    return sorted(data, reverse=True)