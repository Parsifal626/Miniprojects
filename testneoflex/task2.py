"""
Перемещение нулей в массиве
Необходимо написать функцию, которая берет массив и перемещает все нули в конец,
сохраняя порядок остальных элементов.
Пример вывода функции:
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


"""
def move_zeros(arr):
    zeros = []
    non_zeros = []
    for item in arr:
        if item == 0:
            zeros.append(item)
        else:
            non_zeros.append(item)
    return non_zeros + zeros

if __name__ == '__main__':
    arr = input("Введите массив через запятую: ")
    arr = [int(x) for x in arr.split(",")]
    print(move_zeros(arr))
    