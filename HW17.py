two_d_list = [['a', 'c', 'e'],
              ['f', 'b', 'a'],
              ['a', 'n', 'k'],
              ['e', 'l', 'i']]

# Создаем пустой список для отсортированных столбцов
sorted_columns = []

# Перебираем столбцы и сортируем их
for j in range(len(two_d_list[0])):
    column = []  # Создаем пустой список для каждого столбца
    for i in range(len(two_d_list)):
        column.append(two_d_list[i][j])  # Добавляем элементы столбца в список
    column.sort()  # Сортируем элементы столбца
    sorted_columns.append(column)  # Добавляем отсортированный столбец в список
print()
