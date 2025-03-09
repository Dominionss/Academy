import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def filter_primes_with_threads(numbers):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return [num for num, is_p in zip(numbers, results) if is_p]


def filter_primes_with_processes(numbers):
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return [num for num, is_p in zip(numbers, results) if is_p]


def main():
    start_time = time.time()
    primes_threads = filter_primes_with_threads(NUMBERS)
    threads_duration = time.time() - start_time

    start_time = time.time()
    primes_processes = filter_primes_with_processes(NUMBERS)
    processes_duration = time.time() - start_time

    print("Primes (ThreadPoolExecutor):", primes_threads)
    print("Time taken (ThreadPoolExecutor):", threads_duration, "seconds")
    print("Primes (ProcessPoolExecutor):", primes_processes)
    print("Time taken (ProcessPoolExecutor):", processes_duration, "seconds")


if __name__ == "__main__":
    main()
