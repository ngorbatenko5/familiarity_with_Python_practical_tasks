# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


n = int(input("Введите трехзначное число "))
a = n // 100 # целочисленный результат деления, отбрасывая дробную часть
b = n % 100 // 10 # получение остатка от деления и, затем целочисленное деление
c = n % 10
print(f'{a + b + c} ({a} + {b} + {c})')
