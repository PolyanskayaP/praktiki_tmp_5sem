#6 вариант
tire = "----------------------"
dx = float(input("введите шаг dx = "))
e = 0.0001
print("точность =",e) 

xn = -1
xk = 1
x = xn
print("      таблица        ")
print("   x   |   y   |  i  ")
print(tire)
while x < xk:
    a = x
    s = a 
    i = 2
    while abs(a) > e:
        a = (x**i)/i
        s = s + a   #сумма
        i = i + 1   #количество
    s = -1 * s
    print("{:4.3f}".format(x),"|","{:4.3f}".format(s),"|",i)
    print(tire) 
    x = x + dx 
