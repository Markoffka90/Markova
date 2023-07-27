#######################################################################
# Функции проверки ввода
def only_numbers():
    while True:
        try:
            seq = input("Введите последовательность чисел через пробел: ")
            list_numbers = list(map(int, seq.split()))
            return list_numbers
        except ValueError:
            print("Можно вводить только числа. Повторите ввод")

def only_number():
    while True:
        try:
            chislo = int(input('Введите любое число: '))
            return chislo
        except ValueError:
            print("Вы ввели не число. Повторите ввод")
#######################################################################
# Функция сортировки
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

#######################################################################
# Функция бинарного поиска
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находим середину
    print(middle)
    if middle == len(array)-1:  # если смотрим последний элемент, то не выполнится условие про следующий элемент
        return False  # значит элемент отсутствует
    else:
        if array[middle] < element and array[middle+1] >= element:  # если элемент меньше введенного пользователем числа, а следующий за ним больше или равен этому числу
            return middle+1  # возвращаем этот индекс
        elif element <= array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
            return binary_search(array, element, middle + 1, right)

#######################################################################
# Программа
# 1 пункт
list_numbers = only_numbers() # ввод через функцию с проверкой на числа
chislo = only_number() # ввод через функцию с проверкой на число

# 2 пункт
list_numbers = merge_sort(list_numbers)

# 3 пункт
result = binary_search(list_numbers, chislo, 0,  len(list_numbers)-1)

print('Упорядоченный список: ', list_numbers)
if not result:
    print('Нет элементов, удовлетворяющих условию')
else:
    print('Индекс найденного элемента: ', result-1)
