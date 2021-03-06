#1, Напишите программу для случайного выбора элемента из списка.
# Подсказка: Использовать библиотеку random, и функцию choice
# чтобы выбирать разный цвет.

                  

# Код писать ниже(докончить код):
import


#                   Примерный результат:                  Примерный результат:                                                              
#                   Выбранный цвет: Зеленый               Выбранный цвет: Белый 



#2, Напишите программу для умножения всех элементов в списке.
                                              
# Код писать ниже(вместо многоточия написать код):         
# Подсказка, использовать цикл for:                            

arr = [3, 5, 8, 12]
...

for i in arr:
    ...
    
#                                   Результат: 1440






#3, Напишите программу, чтобы получить наибольшее число из списка.

# Подсказка: Использовать цикл for и условные операторы(if, else).
# Код писать ниже(вместо многоточия написать код):
                                        
arr = [23, 444, 5555, 12]
max = arr[...]
for ... in ...:
    if ...:
        

#                                   Результат: 5555





#4, Напишите программу для создания и печати списка из первых и
#   последних 5 элементов, где значения являются квадратами
#   чисел от 1 до 30 (оба включены).

#   Подсказка, если промежуток = от 1 до 30(включены) то, код писать ниже:                                                         

arr = []
for i in range(...):
    ...
 


#                                   Результат:

#                                   [1, 4, 9, 16, 25]                                                
#                                   [676, 729, 784, 841, 900]                                        


#5, Напишите программу для удаления дубликатов из списка.

# Подсказка: цикл for; условные операторы(if, else); метод append.
# Код писать ниже:

arr = [10,20,30,20,10,50,60,40,80,50,40]
...
for ... in arr:
    if ... not in ...:
        ...



#                                   Результат: [10, 20, 30, 50, 60, 40, 80]


#6, Напишите программу для получения суммы всех чисел, которые даны в [].

# Подсказка: цикл for, создать счетчик.                                  
# Код писать ниже:

arr = [3,4,1,8,-7,20,85]
...
for ...:
    



#                                   Результат:

#                                   sum:  114



#7, Есть 2 списка: arr = [2, 4, 16, 78], twice = [0, 0, 0, 0].
#   Напишите программу так, чтобы второй список twice заполнялся
#   значениями из списка a, но в два раза больше.

arr = [13,-4,82,17]
twice = [0,0,0,0]
...
    ...
print (twice)


#                                   Результат: [26, -8, 164, 34]  


#8, У вас есть 3 списка: arr1 = [2, -22, 82, 17],arr2 = [-12, 24, -79, -13],sum = [0, 0, 0, 0].
#   Заполните третий список sum сложив 2 списка, то есть a и b.

# Код писать ниже:

arr1 = [13,-22,82,17]
arr2 = [-12,24,-79,-13]
sum = [0,0,0,0]
...
    ...
print(sum)


#                                   Результат: [-10, 2, 3, 4]


#9, Представьте, что у вас есть 2 списка arr1 = [13, - 22, 82, 17],
#   arr2 = []. Заполните список arr2 соответствующими значениями,
#   чтобы при добавлении их со списком b результат будет 25.

# Код писать ниже:

arr1 = [100,-76,23,17]
arr2 = []
...
    ...
        ...
print (b)


#                                   Результат: [-75, 101, 2, 8]






#10, Напишите программу, которая считает количество четных и нечетных чисел в списке.

# Подсказка: цикл for; условные операторы(if, else)
# Код писать ниже:

arr = [23, 45, 222, 12, 90, 88]
even = 0
odd = 0
...
    ...
        ...


print("Четные:", even)
print("Нечетные:", odd)
print(a)


#                                   Результат:

#                                   Even: 4
#                                   Odd: 2
#                                   [23, 45, 222, 12, 90, 88]




#11,Напишите программу, которая разделяет элементы списка на положительные и отрицательные числа.

# Код писать ниже:

arr = [-23, 44, 45, -90, -876, 120]
neg = []
pos = []
...
    ...
        ...
            ...

print("Отрицательные числа: ",neg)
print("Положительные числа: ",pos)


#                                   Результат:

#                                   Отрицательные числа: [-23, -90, -876]
#                                   Положительные числа: [44, 45, 120]




#12, Дан список целых чисел. Напишите программу, которая заменит отрицательные
#    на число -1, положительные на число 1, 0 оставит без изменений.

# Код писать ниже:

oldList = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
newList = []
...
    ...
        ...
            ...

print("Старый список: ",oldList)
print("Новый список: ",newList)


#                                   Результат:

#                                   Старый список: [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
#                                   Новый список:  [1, -1, 1, 1, 0, 1, -1, 1, -1, 1]




#13, Напишите программу, которая берет список и возвращает новый список,
#    содержащий все элементы первого списка без дубликатов.

# Подсказка: цикл for, метод append.
# Код писать ниже:

a = [1,2,3,4,3,2,1]
y = []
...
    ...
        ...
print(y)


#                                   Результат: [1, 2, 3, 4]




#14, Напишите программу, которая находит среднее арифметическое значение,
#    минимальный элемент и индекс минимального элемента, и в конце выводит список. 

# Подсказка: в результате перед инпутом стоят числа это индексы вводимых вами чисел до 10.
# Код писать ниже: 
arr = []
count = 0 # количество элементов
summa = 0 # счетчик
 
for i in range(10):
	num = input(' Введите число: ')
	...
            ...
                ...
 
if count != 0:
    ...
        ...
            ...
                ...
	print("Среднее арифметическое: ",mean)
	print("Значение минимального элемента в списке: ",minimal)
	print("Индекс минимального элемента: ",min_id)
	print(arr)

#                                   Результат:

#                                   0 number: 3
#                                   1 number: 1
#                                   2 number: 0
#                                   3 number: -1
#                                   4 number: 34
#                                   5 number: 2
#                                   6 number: 2
#                                   7 number: 2
#                                   8 number: 7
#                                   9 number: 8
#                                   Среднее арифметическое:  5.8
#                                   Значение минимального элемента в списке:  -1
#                                   Индекс минимального элемента:  3
#                                   [3, 1, 0, -1, 34, 2, 2, 2, 7, 8]




#15, Допустим, у нас есть список чисел, из которого надо удалить элементы,
#    по определенному условию. Будем удалять из списка, в диапазоне от 0 до 50,
#    все элементы, которые больше 35 и меньше 65. При этом удаляемые числа
#    сохраним в другом списке.

import random
arr1 = []
for i in range(10):
        n = random.randint(0,51) # от 0 до 50 включительно
        ...
print("A = ",arr1)
 
arr2 = []
...
    ...
        ...
            ...
            
print("A = ",arr1)
print("B = ",arr2)

#                                       Результат:

# A = [4, 45, 31, 50, 21, 43, 34, 0, 3, 40]  - изначальный список с рандомными числами
# A = [4, 21, 0, 3] - список с удаленными числами
# B = [45, 31, 50, 43, 34, 40] - список без удаленных чисел



#16, Написать программу, которая собирает четные числа в начало списка, нечетные - в конец.
# Подсказка: цикл for(для определения сколько чисел будут введены),
# методы: append, insert, if-else.

arr = []
...
    n = int(input("Введите число: "))
        ...
            ...

print(a)


#                                   Результат:

#                                   Введите число: 3
#                                   Введите число: 2
#                                   Введите число: 4
#                                   Введите число: 0
#                                   Введите число: 1
#                                   Введите число: 2
#                                   [2, 0, 4, 2, 3, 1]




#17, Напишите программу, которая преобразует текст в список слов с удалением знаков препинания.
# Подсказка: дополнить код с условными операторами(if-else).

sent = input("Напиши текст:\n")
punctuation = [...] # заполнить список с пунктуационными знаками
wordList = sent.split()

i = 0
for word in wordList:
    ...
        ...
            ...
                ...

        i += 1 #переход к следующему слову

print(wordList)

#                               Результат:

#                               Напиши текст:
#                               hello, how are you? 
#                               ['hello', 'how', 'are', 'you']




#18, Напишите программу, которая будет находить элемент, ближайший к нулю.

arr=[-1,2,7,9,-5,98,24,54]
...
    ...
        ...
            ...

print ("Число ближайшее к нулю: ",...)

#                               Результат:

#                               Число ближайшее к нулю: -1




#19, Напишите программу, чтобы она печатала значения в списке в обратном порядке.

arr = [3,2,5,7,9,-1,98,24,54]
...
    ...
        ...
            ...
print(..., end = " ")

#                               Результат: 54 24 98 -1 9 7 5 2 3 



#20, Напишите программу, которая считает сумму чисел стоящих на четных местах
#    и сумму четных чисел стоящих на нечетных местах.

data = [3,2,5,7,9,-5,98,24,54]
sum1 = 0
sum2 = 0
...
    ...
        ...
            ...
                ...

print ("Сумма чисел стоящих на четных местах: ", sum1)
print ("Сумма четных чисел стоящих на нечетных местах: ", sum2)

#                                   Результат:

#                                   Сумма чисел стоящих на четных местах: 169
#                                   Сумма четных чисел стоящих на нечетных местах: 26

