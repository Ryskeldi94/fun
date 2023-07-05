# import math

# a = math.sqrt(16)
# b = math.sin(45)
# c = math.cos(45)
# d = math.log10(100)
# f = math.factorial(3)

# print(a,b,c,d,f)
#==========================================
# import random

# #функция возвращает случайное число с 
# #плавающей запятой в диапазоне от 0.0 до 1.0
# num = random.random()
# print(num)

# # функция возвращает случайное целое число в диапазоне от a до b
# num = random.randint(1, 10)
# print(num)

# #функция выбирает случайный элемент из заданной последовательности.
# fruits = ['apple', 'banana', 'orange']
# random_fruit = random.choice(fruits)
# print(random_fruit)

# #функция случайным образом перемешивает элементы в заданной последовательности
# cards = ['Ace', 'King', 'Queen', 'Jack']
# random.shuffle(cards)
# print(cards)
#==============================================================================
import tkinter as tk

# Создание окна
window = tk.Tk()

# Создание холста
canvas = tk.Canvas(window, width=600, height=300)
canvas.pack()


# Функция для рисования буквы R
def draw_R():
    canvas.create_line(60, 150, 60, 50, width=2)
    canvas.create_line(60,100,95,150,width=2)
    canvas.create_arc(25,50,95,100,start = 270, extent=180, width=2)

# Функция для рисования буквы Y
def draw_Y():
    canvas.create_line(105, 50, 135, 100, width=2)
    canvas.create_line(155,50,135,100,width=2)
    canvas.create_line(135,100,135,150)

# Функция для рисования буквы S
def draw_s():
    canvas.create_arc(165, 50, 200, 100, start=50, extent=220, width=2, style=tk.ARC)  # Верхняя дуга
    canvas.create_arc(165, 100, 200, 150, start=200, extent=250, width=2, style=tk.ARC)  # Нижняя дуга

# Функция для рисования буквы K
def draw_k():
    canvas.create_line(210, 150, 210, 50, width=2)
    canvas.create_line(210,100,250,50, width=2)
    canvas.create_line(210,100,250, 150, width=2)

# Функция для рисования буквы E
def draw_e():
    canvas.create_line(260,50,260,150,width=2)
    canvas.create_line(260,50,300,50,width=2)
    canvas.create_line(260,100,300,100,width=2)
    canvas.create_line(260,150,300,150,width=2)

# Функция для рисования буквы L
def draw_l():
    canvas.create_line(310,50,310,150,width=2)
    canvas.create_line(310,150,350,150,width=2)

# Функция для рисования буквы D
def draw_d():
    canvas.create_arc(320,50,400,150,start=270,extent=180,width=2,)

# Функция для рисования буквы I
def draw_i():
    canvas.create_line(440,50,440,150, width=2)
    canvas.create_line(420,50,460,50,width=2)
    canvas.create_line(420,150,460,150,width=2)
    
# Вызов функций для рисования каждой буквы
draw_R()
draw_Y()
draw_s()
draw_k()
draw_e()
draw_l()
draw_d()
draw_i()

# Запуск главного цикла обработки событий
window.mainloop()
