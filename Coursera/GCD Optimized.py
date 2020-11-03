def optimizedGCD(a,b):
    if b==0:
        return a
    aprime=a%b
    return optimizedGCD(b,aprime)
a=int(input())
b=int(input())
print(optimizedGCD(a,b))