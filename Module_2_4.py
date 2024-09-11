#Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле

i = 0
primes = []
not_primes = []
not_prime = False
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range(len(list1)):
    if (list1[i] > 1):
        for j in range(2, list1[i]):
            if (list1[i] % j == 0):
                not_prime = True
                break
            else:
                not_prime = False
        if (not_prime == False): primes.append(list1[i])
        if (not_prime == True): not_primes.append(list1[i])
print("Primes:",primes)
print("Not primes:",not_primes)