x = float(input("x = ")) 

if (x >= -9) and (x < -7):
    print("y = ", 0) 
elif (x >= -7) and (x < -3):
    print("y = ", x+7)
elif (x >= -3) and (x < -2):
    print("y = ", 4) 
elif (x >= -2) and (x < 2):
    print("y1 = 4, y2 = ", x**2)
elif (x >= 2) and (x < 4):
    print("y = ", -2*x + 8)
elif (x >= 4) and (x <= 7):
    print("y = 0")
else:
    print("x не попадает в границы функции")