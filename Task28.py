# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def Sum(a, b):
    if a == 0:
        return b
    else:
        return Sum(a - 1, b + 1)



A = int(input("Введите неотрицательное число A: "))
B = int(input("Введите неотрицательное число B: "))
if A<0 or B<0:
    print ("Введено отрицательное число, исправьте")
else: 
    print(f"{A} + {B} = {Sum(A,B)}")