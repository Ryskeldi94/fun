#номер задача
start = int(input("Задача:"))

#аналог функция switch на других языках
def switch(start):
    #первое задача
    if start == 1:
        a = int(input("Первое число: "))
        b = int(input("Второе число: "))
        e1(a, b)

    #ВТОРОЕ ЗАДАЧА
    if start == 2:
        a = int(input("Первое число: "))
        b = int(input("Второе число: "))
        e2(a, b)

    #третье задача
    if start == 3:
        a = int(input("Первое число: "))
        b = int(input("Второе число: "))
        e3(a,b)

    #4
    if start == 4:
        a= int(input("Сколько карта:"))
        b= input("Карты на столе:")
        e4(a,b)

    else:
        print("'1-4' ")

def e1(a, b):
    for i in range(a, b + 1):
        print(i)

def e2(a,b):
    if a>=b:
        for i in range(a, b + 1):
            print(i)
    else:
        for i in range(b,a+1):
            print(i)

def e3(a,b):
    for i in range(a,b-1,-1):
        if i % 2==1:
            print(i)

def e4(a, b):
    total = (a * (a + 1)) // 2
    b_list = [int(num) for num in b.split()]
    sum_card = sum(b_list)
    print(total - sum_card)


re=int(input())
print(re)
switch(start)