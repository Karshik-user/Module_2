#"Условная конструкция. Операторы if, elif, else."

first = int(input("Ввидите любое число: "))
second = int(input("Ввидите любое число: "))
third = int(input("Ввидите любое число: "))
if first == second == third:
    print('3')
elif first == second:
    print('2')
elif first == third:
    print('2')
elif second == third:
    print('2')
else:
    print('0')