#9 вариант 
#размерность с клавиатуры, ввод - случайно или нет 
#numpy с массивами
# Aij | Akl  i-1 <= k <= i+1       j-1 <= l <= j+1  

n = int(input("сколько строк в матрице? "))
m = int(input("сколько столбцов в матрице? "))
#rand

A = [] 
for i in range(n): 
    A.append( [0]*m )

S = []
for i in range(n):
    A.append( [0]*m )  

for i in range(n):
    for j in range(m):
        #print(A[i][j]) 
        s = 0; #??? 
        kolv = 0
        for k in range(i-1,i+2):
            for l in range(j-1,j+2):
                if (k,l) != (i,j):
                    s = s + A[k][l]  
                    kolv = kolv + 1 
        s = s / kolv 
        S[i][j] = s 

