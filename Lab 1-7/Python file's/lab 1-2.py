# приветственное сообщение 
print("Hello! My name is Ryskul Ryskeldi")

# Запрашиваем возраст пользователя и сохраняем в переменную "old"
old = int(input("How old are you?"))

# Проверяем условия возраста и выводим соответствующее сообщение
if old < 16:
    print("I'm "  + str(old) + " years old and I'm in school")
elif 17 <= old <= 21:
    print("I'm "  + str(old) + " years old and I'm a student")
else:
    print("I'm "  + str(old) + " years old and I'm working")

print("Hw you name?")