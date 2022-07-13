
nums = input("Введите числа через пробел: ")
num = int(input("Введите число: "))
list_nums = [int(x) for x in nums.split(" ")]


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


list_nums = merge_sort(list_nums)
print(list_nums)


def binary_search(array, element, left, right):
    try:
        if left > right:
            return False

        middle = (right + left) // 2
        if array[middle] == array[0]:
            return "Число равно первому числу списка." \
                   "Введите корректные данные."
        if array[middle] == element:
            return middle - 1
        elif array[middle] < element < array[middle + 1]:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return "Число выходит за диапазон списка." \
               "Введите корректные данные."


print(binary_search(list_nums, num, 0, len(list_nums)))
