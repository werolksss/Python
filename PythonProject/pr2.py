# сортировка по убыванию (пузырьковая)
def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:  # меняем знак сравнения
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


#проверка и сортировка по убыванию
def check_and_sort_desc(arr):
    # Проверяем, упорядочен ли массив по убыванию
    is_sorted = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

    if not is_sorted:
        return bubble_sort_desc(arr.copy())
    return arr


# сортировка четных элементов пузырьком
def sort_even_elements(arr):
    even_elements = [arr[i] for i in range(len(arr)) if i % 2 == 0]

    n = len(even_elements)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if even_elements[j] > even_elements[j + 1]:
                even_elements[j], even_elements[j + 1] = even_elements[j + 1], even_elements[j]

    result = arr.copy()
    even_idx = 0
    for i in range(len(result)):
        if i % 2 == 0:
            result[i] = even_elements[even_idx]
            even_idx += 1

    return result

# сортировка нечетных по возрастанию, четных по убыванию
def sort_odd_even_special(arr):
    odd_positions = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    even_positions = [arr[i] for i in range(len(arr)) if i % 2 == 1]

    odd_positions.sort()
    even_positions.sort(reverse=True)

    result = []
    for i in range(len(arr)):
        if i % 2 == 0:
            result.append(odd_positions.pop(0))
        else:
            result.append(even_positions.pop(0))

    return result

def remove_duplicates(arr):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
    return result

def sort_012(arr):
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    count_2 = arr.count(2)

    result = [1] * count_1 + [2] * count_2 + [0] * count_0
    return result

if __name__ == "__main__":
    test_array = [4, 9, 7, 6, 2, 3]
    test_array2 = [30, 53, 11, 35, 17, 42, 21, 84, 75, 61]
    test_array3 = [1, 2, 2, 0, 1, 0, 2, 1]

    print("Исходный массив:", test_array)
    print()

    print("1) Сортировка по убыванию:", bubble_sort_desc(test_array.copy()))
    print("2) Проверка и сортировка:", check_and_sort_desc(test_array.copy()))
    print("3) Сортировка четных элементов:", sort_even_elements(test_array.copy()))
    print()

    print("Доп 1) Специальная сортировка:", sort_odd_even_special(test_array.copy()))
    print("Доп 2) Без дубликатов:", remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 5]))
    print("Доп 3) Сортировка 0,1,2:", sort_012(test_array3.copy()))