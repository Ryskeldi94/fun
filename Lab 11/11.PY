import tkinter as tk

# Создание окна
window = tk.Tk()

# Создание холста
canvas = tk.Canvas(window, width=4000, height=2000)
canvas.pack()

# Рисование буквы S
# canvas.create_arc(50, 50, 150, 150, start=50, extent=220, width=2, style=tk.ARC)  # Верхняя дуга
# canvas.create_arc(50, 150, 150, 250, start=200, extent=250, width=2, style=tk.ARC)  # Нижняя дуга
canvas.create_line(100,100,0,0)
# Запуск главного цикла обработки событий
window.mainloop()
