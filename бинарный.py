def binary(num_list, number):
    first = 0
    last = len(num_list) - 1
    while first <= last:
        middle = first + (last - first) // 2

        if num_list[middle] == number:
            return middle
        elif num_list[middle] < number:
            first = middle + 1
        else:
            last = middle - 1
    return -1


num_list = sorted(sorted(map(int, input().split())))
number = int(input())

result = binary(num_list, number)
print(f"Список: {num_list}")
print(f"Индекс элемента {number}: {result}")


# c помощью библиотеки
from bisect import bisect_left


def binary(num_list, number):
    pos = bisect_left(num_list, number)
    if pos < len(num_list) and num_list[pos] == number:
        return pos
    return -1


num_list = sorted(sorted(map(int, input().split())))
number = int(input())

result = binary(num_list, number)
print(f"Отсортированный список: {num_list}")
print(f"Поиск числа {number}: {result}")


