r = 2
x = float(input("введите x = "))
y = float(input("введите y = "))

if (x*x + y*y <= r*r) and (x <= 0) and (y >= (x-1)**2) or \
    (x*x + y*y >= r*r) and (y<=r) and (x>=0) and (y >= (x-1)**2) or \
        (x*x + y*y <= r*r) and (y <= (x-1)**2) and (x>=1) and (y >=0):
        print("точка попала в область")
else:
    print("точка не попала в область") 