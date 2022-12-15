import math as mt

a = float(input("enter a = "))
b = float(input("enter b = "))

z1 = (mt.cos(a) - mt.cos(b))**2 - (mt.sin(a) - mt.sin(b))**2
z2 = -4 * mt.sin((a-b)/2)**2 * mt.cos(a+b)

print("z1 = ", z1, " z2 = ",z2)