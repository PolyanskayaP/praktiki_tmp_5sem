'''b = array([[1, 2], [0, 1]])

b[:,2] 
b[...] 

b[:,:] 

b[0,...] 
def foo(el, lst = ''): 
    lst+=str(el) 
    return lst 
    foo(1) 
    foo(2) 
    print (foo(3))

foo(23)
foo = (1,) 
bar = foo 
bar += (1,) 
print (foo)
print (-1 + 1 * 3 == 0 or 5 - 3 * 3 > 0)

arr = [1,5,3,2] 
n = 0 
for i in arr: 
    if i%3==0: 
        break 
    elif i<4: 
        n+=i 
        n+=i 
    else: 
        n-=1 
        print (n)

s1, s2, s3 = '0', (), 'None' 
res = s1 and not s2 or not s3 
print (res)
x = ('P','r','i','n','t') 
x[0] = 'p' 
print (x)'''
'''
foo = 13
out = '' 
if foo >= 3: 
    out+='Foo' 
elif foo < 7: 
    out+='bar' 
    if foo < 10: 
        out+='Foo' 
    else: 
        out+='bar' 
        print (out)
'''
'''
print (not -10 + 2 * 4 < -5 and 1 + 5 * 2 > 1)
def fun (a=2, b, *c): 
    for i in c: 
        res=res+i 
        print (res) 

fun(1,2,3,1)'''

for i in range (10, 2):
    print(i)
