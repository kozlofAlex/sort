arr = input('Введите последовательность чисел через пробел: ')
number = int(input('Введите любое число: '))

# Определение чисел в строке
def is_int(str):
    str = str.replace(' ', '') # удаляем пробелы
    try:
        int(str)
        return True
    except ValueError:
        return False

# Проверка ввода только чисел
if not is_int(arr):
    print('Введите только целые числа!')
else:
    arr = arr.split()

# 1. Преобразование последовательности в список
array = list(map(int,arr))

# 2. Сортировка (пузырьком) списка по возрастанию элементов
def sort():
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

array.sort()
print(f'Упорядоченный по возрастанию список: {array}')

# Алгоритм двоичного поиска
def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка'

# Номер позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу
if not binary_search(array, number, 0, len(array)):
    rI = min(array, key=lambda x: (abs(x - number), x))
    ind = array.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < number:
        print(f'''Ближайший меньший элемент =  {rI}, его индекс: {ind}
Ближайший больший элемент =  {array[max_ind]}, индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке отсутствет ближайший меньший элемент 
Ближайший больший элемент: {rI}, индекс: {array.index(rI)}''')
    elif rI > number:
        print(f'''Ближайший больший элемент: {rI}, его индекс: {array.index(rI)}
Ближайший меньший элемент: {array[min_ind]}, его индекс: {min_ind}''')
    elif array.index(rI) == 0:
        print(f'Индекс введенного элемента: {array.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(array, number, 0, len(array))}')
