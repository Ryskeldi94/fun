# def fung(string):
#     u_count = 0
#     l_count = 0

#     # Подсчет букв
#     for char in string:
#         if char.isupper():
#             u_count += 1
#         elif char.islower():
#             l_count += 1

#     # Преобразование строки 
#     if u_count > l_count:
#         print(string.upper())
#     else:
#         print(string.lower())

# input_string = input()
# fung(input_string)
#===========================================================================

while True:
    a = input()
    b = input()

    if a.isdigit() == True and b.isdigit() == True:
        print(int(a) + int(b))
        break