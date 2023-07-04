def display_collection(collection):
    if isinstance(collection, list):
        print("Список:")
        for item in collection:
            print(item)
    elif isinstance(collection, tuple):
        print("Кортеж:")
        for item in collection:
            print(item)
    elif isinstance(collection, set):
        print("Набор:")
        for item in collection:
            print(item)
    elif isinstance(collection, dict):
        print("Словарь:")
        for key, value in collection.items():
            print(key, ":", value)
    else:
        print("Неподдерживаемый тип коллекции.")


print("Выберите тип коллекции:")
print("1. Список")
print("2. Кортеж")
print("3. Набор")
print("4. Словарь")

choice = int(input("Введите номер выбора: "))

if choice == 1:
    collection = ["Ryskeldi", "Ryskul", "Almaty"]
elif choice == 2:
    collection = ("Ryskeldi", "Ryskul", "Almaty")
elif choice == 3:
    collection = {"Ryskedli", "Ryskul", "Almaty"}
elif choice == 4:
    collection = {"1": "Ryskeldi", "2": "Ryskul", "3": "Almaty"}
else:
    print("Неверный выбор.")
    exit()

display_collection(collection)
