s='-----------------------'
print('        Таблица')
print(s)
print('|   x   |      y      |')
print(s)
for x in range(-9,10,2):
    if (x >= -9) and (x < -7):
        y = 0
        print('|',"{:5.2f}".format(x),'|', "{:11.4f}".format(y),'|')  
        print(s)
    elif (x >= -7) and (x < -3):
        y = x+7
        print('|',"{:5.2f}".format(x),'|', "{:11.4f}".format(y),'|') 
        print(s)
    elif (x >= -3) and (x < -2):
        y = 4
        print('|',"{:5.2f}".format(x),'|', "{:11.4f}".format(y),'|')  
        print(s)
    elif (x >= -2) and (x < 2):
        y = 4
        y2 = x**2
        print('|',"{:5.2f}".format(x),'|', "{:4.2f}".format(y),',', "{:4.2f}".format(y2),'|') 
        print(s)
    elif (x >= 2) and (x < 4):
        y = -2*x + 8
        print('|',"{:5.2f}".format(x),'|', "{:11.4f}".format(y),'|') 
        print(s)
    elif (x >= 4) and (x <= 7):
        y = 0
        print('|',"{:5.2f}".format(x),'|', "{:11.4f}".format(y),'|') 
        print(s)
    else:
        print('|',"{:5.2f}".format(x),'|', 'не попадает |') 
print(s)