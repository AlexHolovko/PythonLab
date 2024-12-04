#Завдання 1: Капелюх і список

hat_list = [1, 2, 3, 4, 5]

hat_list[2] = int(input("Введіть ціле число для заміни третього елемента списку: "))

hat_list.pop()
print("Довжина списку:", len(hat_list))
#Завдання 2: Сортування методом бульбашки
def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# Тестовий список
unsorted_list = [34, 23, 7, 1, 0]
sorted_list = bubble_sort(unsorted_list)
print("Відсортований список:", sorted_list)

#Завдання 3: Видалення дублікатів

original_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("Список без дублікатів:", unique_list)

#Завдання 4: Середньомісячна температура
chessboard = [["_" for _ in range(8)] for _ in range(8)]

chessboard[0][0] = "R"  # Лівий верхній кут
chessboard[0][7] = "R"  # Правий верхній кут
chessboard[7][0] = "R"  # Лівий нижній кут
chessboard[7][7] = "R"  # Правий нижній кут

for row in chessboard:
    print(" ".join(row))
