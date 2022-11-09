#9 вариант 
#размерность с клавиатуры, ввод - случайно или нет 
#numpy с массивами
# Aij | Akl  i-1 <= k <= i+1       j-1 <= l <= j+1  
from random import uniform 

n = int(input("сколько строк в матрице? "))
m = int(input("сколько столбцов в матрице? "))

A = [] 
for i in range(n): 
    A.append( [0]*m )

S = []
for i in range(n):
    S.append( [0]*m )  


f = int(input("Введите, если: массив наполнить рандомно 0, с клавиатуры 1   ")) 
if f:
    for i in range(n):
        for j in range(m):
            A[i][j] = float(input(f'введите элемент:A[{i}][{j}]=')) 
else:
    for i in range(n):
        for j in range(m):
            A[i][j] = uniform(1,30)

def sglazhivanie(A,S,n,m):
    for i in range(n):
        for j in range(m):
            s = 0; 
            kolv = 0
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if ((k,l) != (i,j)) and (k>=0) and (l>=0) and (k<n) and (l<m):
                        s = s + A[k][l]  
                        kolv = kolv + 1         
            if kolv>0:
                s = s / kolv 
            S[i][j] = s 

sglazhivanie(A,S,n,m) 

def sum_abs_niz_gd(S, n, m):
    summ = 0
    for i in range(n):
        for j in range(m):
            if i>j:
                summ = summ + abs(S[i][j])
    return summ

print("A:")
for i in range(n):
    for j in range(m):
        print(A[i][j], end=" ")
    print()

print("S:") 
for i in range(n):
    for j in range(m):
        print(S[i][j], end=" ")
    print()  

print()
print(f"Сумма модулей элементов, расположенных ниже главной диагонали = {sum_abs_niz_gd(S,n,m)}")
