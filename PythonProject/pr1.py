import random
import time

#массив
def generate_array(n):
    return [random.randint(0, 100000) for _ in range(n)]
# bubble sort
def bubble_sort(arr):
    a = arr.copy()
    swaps = 0
    start = time.time()
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    end = time.time()
    return end - start, swaps


# selection sort
def selection_sort(arr):
    a = arr.copy()
    swaps = 0
    start = time.time()
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        swaps += 1
    end = time.time()
    return end - start, swaps


# insertion sort
def insertion_sort(arr):
    a = arr.copy()
    swaps = 0
    start = time.time()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            swaps += 1
            j -= 1
        a[j + 1] = key
    end = time.time()
    return end - start, swaps


#quick sort
def quick_sort(arr):
    swaps = [0]
    start = time.time()

    def _quick(a):
        if len(a) <= 1:
            return a
        pivot = a[len(a)//2]
        left = [x for x in a if x < pivot]
        middle = [x for x in a if x == pivot]
        right = [x for x in a if x > pivot]
        swaps[0] += len(left) + len(right)
        return _quick(left) + middle + _quick(right)

    _quick(arr.copy())
    end = time.time()
    return end - start, swaps[0]


# merge sort
def merge_sort(arr):
    swaps = [0]
    start = time.time()

    def _merge(a):
        if len(a) > 1:
            mid = len(a)//2
            L = a[:mid]
            R = a[mid:]
            _merge(L)
            _merge(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    a[k] = L[i]
                    i += 1
                else:
                    a[k] = R[j]
                    j += 1
                swaps[0] += 1
                k += 1
            while i < len(L):
                a[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                a[k] = R[j]
                j += 1
                k += 1

    _merge(arr.copy())
    end = time.time()
    return end - start, swaps[0]


# shaker sort
def shaker_sort(arr):
    a = arr.copy()
    swaps = 0
    start = time.time()
    left = 0
    right = len(a) - 1
    while left <= right:
        for i in range(left, right):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swaps += 1
        right -= 1
        for i in range(right, left, -1):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
                swaps += 1
        left += 1
    end = time.time()
    return end - start, swaps


#
def run_experiment():
    sizes = [1000, 10000, 100000]
    methods = {
        "Bubble": bubble_sort,
        "Selection": selection_sort,
        "Insertion": insertion_sort,
        "Quick": quick_sort,
        "Merge": merge_sort,
        "Shaker": shaker_sort
    }

    for n in sizes:
        arr = generate_array(n)
        print(f"\nРазмер массива: {n} ")
        for name, func in methods.items():
            best_time = float("inf")
            best_swaps = 0
            for _ in range(5):  # 5 запусков
                t, s = func(arr)
                if t < best_time:
                    best_time, best_swaps = t, s
            print(f"{name:10} / Время: {best_time:.5f} сек / Перестановок: {best_swaps}")


# ---------- Запуск ----------
if __name__ == "__main__":
    run_experiment()
