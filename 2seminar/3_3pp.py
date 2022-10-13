#6 вариант 

#x = float(input("введите х = "))
#y = float(input("введите у = "))
dx = float(input("введите шаг dx = "))
e = float(input("введите точность = "))

xn = -1
xk = 1
x = xn
while x < xk:
    a = x
    s = a 
    i = 2
    while abs(a) > e:
        a = (x**i)/i
        s = s + a   #сумма
        i = i + 1   #количество
    s = -1 * s
    print("x=","{:4.3f}".format(x)," y=","{:4.3f}".format(s)," i=",i)
    x = x + dx 
