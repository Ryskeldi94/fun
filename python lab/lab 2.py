#my first python file for git

#приветственное сообщение 
print("Hello! My name is Ryskul Ryskeldi")

# Запрашиваем возраст пользователя и сохраняем в переменную "a"
a = int(input("How old are you?"))

# Проверяем условия возраста и выводим соответствующее сообщение
if a < 16:
    print("I'm "  + str(a) + " years old and I'm in school")
elif 17 <= a <= 21:
    print("I'm "  + str(a) + " years old and I'm a student")
else:
    print("I'm "  + str(a) + " years old and I'm working")
