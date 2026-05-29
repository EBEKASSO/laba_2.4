try:
    numbers = list(map(int, input("Введите числа через пробел: ").split()))
except ValueError:
    print("Ошибка: введите числа!")
    exit()

# 1. Записываем исходные числа
with open("resource/count.txt", "w") as file:
    file.write(" ".join(map(str, numbers)) + "\n")

# 2. Константа
x = 73 ** 2 + 29  # 5358
temp_path = "resource/count_tmp.txt"

# 3. Читаем -> обрабатываем -> пишем во временный файл
with open("resource/count.txt", "r") as src, open(temp_path, "w") as tmp:
    for line in src:
        processed = []
        for token in line.split():
            num = int(token)
            if num % 7 == 0:
                # Округляем до 2 знаков для читаемости
                num = round(num * 100 / x, 2)
            processed.append(str(num))
        tmp.write(" ".join(processed) + "\n")

# 4. Заменяем исходный файл обработанным (выполняется ПОСЛЕ закрытия файлов выше)
with open(temp_path, "r") as tmp, open("resource/count.txt", "w") as dst:
    for line in tmp:
        dst.write(line)

print("Файл успешно обработан.")
