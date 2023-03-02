# QAP-105 Задание 22.9.1 (HW-03) (Codepage=UTF-8)

def bubble_sort(sort_array):
    n = len(sort_array)
    for i in (range(n)):
        for j in range(n - i - 1):
            if sort_array[j] > sort_array[j + 1]:
                sort_array[j], sort_array[j + 1] = sort_array[j + 1], sort_array[j]
    return sort_array


def binary_search_less(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element >= array[middle - 1]:
        return middle-1
    if array[middle] < element <= array[middle + 1]:
        return middle
    elif element < array[middle]:
        return binary_search_less(array, element, left, middle - 1)
    else:
        return binary_search_less(array, element, middle + 1, right)


def user_input_array():
    while True:
        print('Введите последовательность чисел разделенных пробелами\n\tНапример: 1 3 6.7 12 3e2 -1')
        user_input = input('-->')
        try:
            user_array = [float(i) if '.' in i or 'e' in i else int(i) for i in user_input.lstrip().rstrip().split(' ')]
            break
        except ValueError:
            print('\033[31mПри вводе данных необходимо использовать только числа разделенные пробелами!\033[0m\n')
            continue
    return user_array


def user_input_number():
    while True:
        print('Введите число относительно которого будет произведен поиск позиции в последовательности')
        user_input = input('-->')
        try:
            number = float(user_input)
            break
        except ValueError:
            print('\033[31mПри вводе данных необходимо использовать только цифры!\033[0m\n')
            continue
    return number


print('\nПрограмма поиска номера позиции элемента,\nкоторый:\n\t\tменьше введенного пользователем числа,'
      '\n\t\tследующий за ним элемент больше или равен этому числу'
      '\n\t\t(позицию в списке считать начиная с 1)\n')
while True:
    array_s = user_input_array()
    if len(array_s) > 1:
        break
    else:
        print('В последовательности меньше двух чисел\n')
        continue

element_s = user_input_number()

print('Вы ввели последовательность:')
print('\t',  array_s)
print('Последовательность после пузырьковой сортировки:')
print('\t', bubble_sort(array_s))
if array_s[0] >= element_s:
    print(f'\nОтвет не найден. В последовательности отсутствует элемент меньше заданного числа ({element_s})')
elif array_s[-1] < element_s:
    print(f'\nОтвет не найден. Последний элемент в последовательности ({array_s[-1]}) '
          f'меньше заданного числа ({element_s})')
else:
    dln = binary_search_less(array_s, element_s, 0, len(array_s))
    print(f'Ответ:\n\tэлемент на {dln+1}-й позиции со значением {array_s[dln]} меньше заданного числа ({element_s})')
