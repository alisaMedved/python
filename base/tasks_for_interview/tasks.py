import math
from functools import reduce
from copy import deepcopy

# функция факториала

def factorial(n):
    if n == 0:
        return 1
    return reduce(lambda acc, elm: acc*elm,list(range(1, n+1)), 1)

print(factorial(5))
print(5*4*3*2*1)

# Быстрая сортировка - бинарная сортировка
arr = [1, 6, 9, 3, 20, 9, 11, -11, 5, 8, 3]

def quick_sort(not_sorted_arr):
    if len(not_sorted_arr) <= 1:
        return not_sorted_arr
    pivot_index = math.floor(len(not_sorted_arr)/2)
    pivot = not_sorted_arr[pivot_index]
    grater = []
    less = []
    for elm in not_sorted_arr:
        if elm < pivot:
            less.append(elm)
        elif elm > pivot:
            grater.append(elm)
        else:
            continue
    return quick_sort(less) + [pivot] + quick_sort(grater)

sorted_arr = quick_sort(arr)

print(sorted_arr)

# бинарный поиск
def binary_search(sorted_list, searched_elm):

    result = {
        'left': 0,
        'right': len(sorted_list) - 1,
    }

    def inner_fn(sorted_list, searched_elm, res):
        print(f'res: {res}')
        res_deep_copy = deepcopy(res)
        middle_from_res = math.ceil((res_deep_copy['left'] + res_deep_copy['right'])/2)
        if len(sorted_list) == 0:
            raise IndexError('list is empty')
        if len(sorted_list) == 1:
            return middle_from_res if searched_elm == sorted_list[0] else -1

        left = 0
        right = len(sorted_list) - 1
        middle_index = math.floor(len(sorted_list) / 2)
        middle_elm = sorted_list[middle_index]

        if searched_elm == middle_elm:
            return middle_from_res
        elif searched_elm < middle_elm:
            right = middle_index - 1
            res_deep_copy['right'] = res_deep_copy['right'] - len(sorted_list) + right + 1
        elif searched_elm > middle_elm:
            left = middle_index + 1
            res_deep_copy['left'] = res_deep_copy['left'] + left
        else:
            return -1
        return inner_fn(sorted_list[left: right + 1:], searched_elm, res_deep_copy)

    return f'{sorted_list}\nsorted_list[{inner_fn(sorted_list, searched_elm, result)}]: {searched_elm}'

searched_index = binary_search(sorted_arr, 9)
print(searched_index)

searched_index_1 = binary_search(sorted_arr, 20)
print(searched_index_1)


searched_index_2 = binary_search(sorted_arr, -11)
print(searched_index_2)


searched_index_3 = binary_search(sorted_arr, 3)
print(searched_index_3)

searched_index_4 = binary_search(sorted_arr, 5)
print(searched_index_4)

searched_index_5 = binary_search(sorted_arr, 4)
print(searched_index_5)

searched_index_6 = binary_search(sorted_arr, 7)
print(searched_index_6)

