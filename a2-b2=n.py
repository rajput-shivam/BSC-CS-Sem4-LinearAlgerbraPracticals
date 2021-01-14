#a2-b2=N

import math

def check_perfect_sqr(num):
    root=math.sqrt(num)
    if int(root+0.5)**2 == number:
        return true
    else:
        return false


n=int(input("enter N:"))
for i in range(0,100):
    if check_perfect_sqr(i):
        a=i
        b=math.sqrt(n+i*i)
        print(str(a)+"^2-"+str(b)+"^2="+str(n))

