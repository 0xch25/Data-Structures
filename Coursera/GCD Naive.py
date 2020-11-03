def gcd(a,b):
    best=0
    for i in range(1,a+b):
        if (a%i==0) and (b%i==0):
            best=i
    return best

a=int(input())
b=int(input())
print(gcd(a,b))

'''

a=3918848
b=1653264
output:61232
'''