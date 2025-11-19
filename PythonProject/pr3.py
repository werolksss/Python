import timeit
import cProfile
import multiprocessing
from functools import lru_cache


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


@lru_cache(maxsize=128)
def factorial_cached(n):
    if n <= 1:
        return 1
    return n * factorial_cached(n - 1)


def factorial_worker(args):
    start, end = args
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


def factorial_parallel(n, processes=4):
    if n == 0:
        return 1

    chunk = n // processes
    ranges = []

    for i in range(processes):
        start = i * chunk + 1
        end = (i + 1) * chunk if i < processes - 1 else n
        if start <= end:
            ranges.append((start, end))

    with multiprocessing.Pool(processes=processes) as pool:
        results = pool.map(factorial_worker, ranges)

    result = 1
    for res in results:
        result *= res
    return result


def test_performance(func, values, runs=1000):
    results = {}
    for n in values:
        def test_func():
            return func(n)

        timer = timeit.Timer(test_func)
        total_time = timer.timeit(number=runs)
        avg_time = total_time / runs

        results[n] = {
            'avg': avg_time,
            'total': total_time,
            'result': func(n)
        }
    return results


def main():
    n_values = [10, 20, 30]
    runs = 1000

    print("Рекурсивный метод:")
    recursive = test_performance(factorial_recursive, n_values, runs)
    for n in n_values:
        r = recursive[n]
        print(f"n={n}: {r['avg']:.8f} сек")

    print("\nИтерационный метод:")
    iterative = test_performance(factorial_iterative, n_values, runs)
    for n in n_values:
        r = iterative[n]
        print(f"n={n}: {r['avg']:.8f} сек")

    print("\nС кэшированием:")
    cached = test_performance(factorial_cached, n_values, runs)
    for n in n_values:
        r = cached[n]
        print(f"n={n}: {r['avg']:.8f} сек")

    print("\nПараллельный метод:")
    parallel = test_performance(factorial_parallel, n_values, runs)
    for n in n_values:
        r = parallel[n]
        print(f"n={n}: {r['avg']:.8f} сек")

    print("\nСравнение для n=20:")
    methods = {
        'Рекурсивный': recursive[20]['avg'],
        'Итерационный': iterative[20]['avg'],
        'С кэшированием': cached[20]['avg'],
        'Параллельный': parallel[20]['avg']
    }

    for name, time in methods.items():
        print(f"{name}: {time:.8f} сек")

    print("\nПрофилирование рекурсивного метода:")
    cProfile.run('factorial_recursive(20)')

    print("\nПрофилирование итерационного метода:")
    cProfile.run('factorial_iterative(20)')


if __name__ == "__main__":
    main()