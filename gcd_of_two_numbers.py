def GCD(dividend, divisor):
    rem = dividend%divisor
    if rem==0:
        return divisor
    return GCD(divisor,rem)
    


a=int(input("enter a:"))
b=int(input("enter b:"))
print(GCD(a,b))
