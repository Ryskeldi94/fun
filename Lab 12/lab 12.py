in_file = open('C:\\Users\\rrysk\\OneDrive\\Документы\\Функционал\\Lab 12\\input.txt', 'r')
cin_file = open('C:\\Users\\rrysk\\OneDrive\\Документы\\Функционал\\Lab 12\\output.txt', 'w', encoding='utf-8')

for line in in_file:
    # Преобразуем строку в список чисел
    numbers = [int(num) for num in line.split()]

    # Вычисляем сумму чисел
    sum_numbers = sum(numbers)

    # Записываем результат в выходной файл
    cin_file.write(f"Сумма чисел: {sum_numbers}\n")

# Закрываем файлы
in_file.close()
cin_file.close()