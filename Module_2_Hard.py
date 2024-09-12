'''Дополнительное практическое задание по модулю*'''

def _numbers(number):
    n = []
    for i in range(3, number+1):
        if number % i == 0:
            n.append(i)
    return n

def result(number):
    result = []
    for i in range(1, number +1):
        for j in range(1, i + 1):
            if (i + j) % number == 0 and i != j:
                result.insert(0, i)
                result.insert(0, j)
    return result

def password(number):
    password = []
    n = _numbers(number)
    for i in n:
        password += result(i)
    return password

number = int(input('Ключ - '))
password = password(number)
print('Пароль', *password)

#Вариант на основе моего кода от ChatGPT
#Я залил в него свой код (который выше), а он выдал этот как более правильный
#Но я ему не верю))
'''def find_multiple_numbers(number):
    return [i for i in range(3, number + 1) if number % i == 0]

def result(number):
    result = []
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            if (i + j) % number == 0 and i != j:
                result.extend([j, i]) 
    return result

def password(number):
    password_list = []
    multiples = find_multiple_numbers(number)
    for multiple in multiples:
        password_list.extend(result(multiple))
    return password_list

number = int(input('Ключ - '))
generated_password = password(number)
print('Пароль:', *generated_password)
'''