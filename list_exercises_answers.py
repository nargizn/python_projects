'''
#1, Напишите программу для случайного выбора элемента из списка.

import random
spisok_cvetov = ['Красный', 'Синий', 'Зеленый', 'Белый', 'Черный']
print("Выбранный цвет:",random.choice(spisok_cvetov))
'''


'''
#2, Напишите программу для умножения всех элементов в списке.

items = [3, 5, 8, 12]
tot = 1
for x in items:
    tot *= x
print(tot)
'''
'''
#3, Напишите программу, чтобы получить наибольшее число из списка.

arr = [23, 444, 5555, 12]
max = arr[0]
for a in arr:
    if a > max:
        max = a
print(max)
'''

'''
#4, Напишите программу для создания и печати списка из первых и последних 5 элементов, где значения являются квадратами чисел от 1 до 30 (оба включены).

l = []
for i in range(1,31):
    l.append(i**2)
print(l[:5])
print(l[-5:])
'''

'''
#5, Напишите программу для удаления дубликатов из списка.

a = [10,20,30,20,10,50,60,40,80,50,40]
uniq_list = []
for i in a:
    if i not in uniq_list:
        uniq_list.append(i)
print(uniq_list)
'''


'''
#6, Напишите программу для получение суммы всех чисел, которые даны в данном списке [3, 4, 1, 8,­ ‐7, 20, 85].
a = [3,4,1,8,-7,20,85]
sum=0
for n in a:
        sum+=n
print("sum: ", sum)
'''

'''
#7, У вас есть 2 списка: a = [2, 4, 16, 78] и twice = [0, 0, 0, 0]. Напишите программу так, чтобы второй список twice заполнялся значениями из списка a, но в два раза больше.
a = [13,-4,82,17]
twice = [0,0,0,0]
for i in range(len(twice)):
    twice[i]=a[i]*2
print (twice)
'''

'''
#8, У вас есть 3 списка: a = [2, 45, 66, 80], b = [23, 444, 1, 90], sum = [0, 0, 0, 0]. Заполните третий список sum сложив 2 массива(a,b). 
a=[13,-22,82,17]
b=[-12,24,-79,-13]
sum=[0,0,0,0]
for i in range(len(sum)):
	sum[i]=a[i]+b[i]
print(sum)
'''

'''
#9, Представьте, что у вас есть 2 списка a = [13, - 22, 82, 17], b = []. Заполните список b соответствующими значениями, чтобы при добавлении их со списком b результат будет 25.
a=[100,-76,23,17]
b=[]
sum=[25,25,25,25]
for i in range(len(a)):
	b.append(25-a[i])
print (b)
'''

'''
#10, Напишите программу, которая считает количество четных и нечетных чисел в списке.
a = [23, 45, 222, 12, 90, 88]
even = 0
odd = 0

for i in a:
    if i%2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
print(a)
'''

'''
#11,Напишите программу, которая разделяет элементы списка на положительные и отрицательные числа.

a = [-23, 44, 45, -90, -876, 120]
neg = []
pos = []
for i in a:
    if i < 0:
        neg.append(i)
    elif i > 0:
        pos.append(i)
print("Negative numbers: ",neg)
print("Positive numbers: ",pos)
'''

'''
#12, Дан список целых чисел. Напишите программу, которая заменит отрицательные на число -1, положительные на число 1, 0 оставит без изменений.
oldList = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
newList = []
for i in oldList:
    if i > 0:
        newList.append(1)
    elif i < 0:
        newList.append(-1)
    else:
        newList.append(0)

print("Old List: ",oldList)
print("New List: ",newList)
'''

'''
#13, Напишите программу, которая берет список и возвращает новый список, содержащий все элементы первого списка без дубликатов.

a = [1,2,3,4,3,2,1]
y = []
for i in a:
    if i not in y:
        y.append(i)
print(y)
'''

'''
#14, Напишите программу, которая находит среднее арифметическое значение, минимальный элемент и индекс минимального элемента, и в конце выводит список. 

arr = []
count = 0 # количество элементов
summa = 0 # сумма отрицательных элементов
 
for i in range(10):
	num = int(input(str(i) + ' number: '))
	arr.append(num)
	count += 1
	summa += num
 
if count != 0:
	mean = summa/count # среднее арифметическое
	minimal = min(arr) # значение минимального элемента в списке-массиве
	min_id = arr.index(minimal) # индекс минимального элемента 
	#arr[min_id] = round(mean)
	print("Среднее арифметическое: ",mean)
	print("Значение минимального элемента в списке: ",minimal)
	print("Индекс минимального элемента: ",min_id)
	print(arr)
'''

'''
#15, Допустим, у нас есть список чисел, из которого надо удалить элементы, удовлетворяющие определенному условию. Будем удалять из списка, в диапазоне от 0 до 101, все элементы, которые больше 35 и меньше 65. При этом удаляемые числа сохраним в другом списке.

import random
a = []
for i in range(10):
        n = random.randint(0,51) # от 0 до 50 включительно
        a.append(n)
print("A =",a)
 
b = []
i = 0
while i < len(a):
	if 25 < a[i] < 55:
		b.append(a[i])
		del a[i]
	else:
		i += 1
print("A =",a)
print("B =",b)
'''

'''
#16, Написать программу, которая собирает четные числа в начало списка, нечетные - в конец.
a = []
for i in range(6):
    n = int(input("Number: "))
    if n%2 == 0:
        a.insert(0,n)
    else:
        a.append(n)
print(a)
'''

'''
#17, Напишите программу, которая преобразует текст в список слов с удалением знаков препинания.
sent = input("Write down or insert some text:\n")

punctuation = ['.',',',':',';','!','?']

wordList = sent.split()

i = 0
for word in wordList:
    if word[-1] in punctuation: #Если последний символ этого слова содержится в списке punctuation
        wordList[i] = word[:-1] #то на место (i) этого слова в список wordList помещается копия этого слова, но без последнего символа. Срез [:-1] обозначает взять последовательность от ее начала до последнего элемента (не включая его).
        word = wordList[i] # Заменяется значение word на текущее, иначе алгоритм ниже будет обрабатывать старое слово, а не то, у которого уже мог быть удален последний символ.
    if word[0] in punctuation:     # Еще если первый символ слова содержится в списке знаков препинания,
        wordList[i] = word[1:] # то переписать слово на его копию без первого символа.Срез [1:] обозначает взять последовательность от элемента с индексом 1 (он второй по счету) до конца.
    i += 1 #переход к следующему слову
print(wordList)
'''

'''
#18, Напишите программу, которая будет находить элемент, ближайший к нулю.

data=[-1,2,1,7,9,-5,98,24,54]
closest=data[0]
for i in range(len(data)):
    if abs(data[i])<closest:
        closest=data[i]
        
print ("The closet number to zero is: ",closest)
'''

'''
#19, Напишите программу, чтобы она печатала значения в списке в обратном порядке.

data = [3,2,5,7,9,-1,98,24,54]
for i in range(len(data)):
    j = len(data)-1-i
    print (data[j], end=" ")
'''

'''
#20, Напишите программу, которая считает сумму чисел стоящих на четных местах и сумму четных чисел стоящих на нечетных местах.

data = [3,2,5,7,9,-5,98,24,54]
sum1 = 0
sum2 = 0

for i in range(len(data)):
    if i%2==0:
        sum1+=data[i]
for i in range(len(data)):
    if data[i]%2==0 and i%2!=0:
        sum2+=data[i]
        
print ("Sum of numbers that stand on even places: ", sum1)
print ("Sum of even numbers that stand on odd places ", sum2)
'''
