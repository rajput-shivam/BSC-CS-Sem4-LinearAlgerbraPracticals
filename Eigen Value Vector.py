import math

def eigenVector(array,x):
    array[0][0]-=x
    array[1][1]-=x
    print("equation of line:")
    print(array[0][0],"x","+(",array[0][1],")y = 0")
    

array=[[7,3],[3,-1]]
a=array[0][0]
b=array[0][1]
c=array[1][0]
d=array[1][1]
det= (a*a)+(d*d)-(2*a*d)+(4*b*c)
ev1= ((a+d)+math.sqrt(det))/(2)
ev2= ((a+d)-math.sqrt(det))/(2)
print("eigen-value1",ev1)
print("eigen-value2",ev2)

eigenVector(array,ev1)



