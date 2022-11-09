# 6 вариант; 4 - сортировка слиянием 
import random 

def merge_sort(spisok): 
    if len(spisok) > 1: 
        mid = len(spisok)//2
        left = spisok[:mid] 
        right = spisok[mid:]
        merge_sort(left) 
        merge_sort(right) 
        i = j = k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                spisok[k] = left[i] 
                i+=1
            else: 
                spisok[k] = right[j] 
                j+=1
            k+=1
        while i < len(left): 
            spisok[k] = left[i] 
            i+=1
            k+=1
        while j < len(right): 
            spisok[k] = right[j] 
            j+=1
            k+=1

n = int(input("введите количество элементов массива: "))
f = int(input("введите 0, если хотите наполнить массив рандомными числами, иначе введите 1: "))

m = list()

for i in range(n):
    if f:
        a = float(input("введите значение: "))
        m.append(a) 
    else:
        a = random.randint(-2,2)
        m.append(a)
print(m) 
fi = -1
li = -1
min = m[0] 
for i in range(n):  
    if (fi == -1) and (m[i] > 0):
        fi = i 
    if (m[i]>0):
        li = i 
    if m[i]<min:
        min = m[i] 

s = 0
for i in range(fi+1, li):
    s = s + m[i]  
print("сумма эл-тов между первым и последним положительным = ", s)
print("минимальный элемент = ", min)

shi = 0
for i in range(n):
    if m[i] == 0:
        m[shi], m[i] = m[i], m[shi]
        shi = shi + 1 

print("сначала 0(если есть), потом остальное: ")
print(m) 

#сортировка слиянием 
print("отсортированный слиянием массив:")
merge_sort(m)
print(m) 
    
