r = 2
n = int(input("сколько выстрелов будет? = "))

for i in range(n):
    x = float(input("введите x = "))
    y = float(input("введите y = "))

    if (x*x + y*y <= r*r) and (x <= 0) and (y >= (x-1)**2) or \
        (x*x + y*y >= r*r) and (y<=r) and (x>=0) and (y >= (x-1)**2) or \
            (x*x + y*y <= r*r) and (y <= (x-1)**2) and (x>=1) and (y >=0):
            print("при x=",x, " и y=",y,"вы попали в мишень")
    else:
        print("при x=",x, " и y=",y,"вы НЕ попали в мишень")