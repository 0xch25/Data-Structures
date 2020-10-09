# Write your code here
s,k=map(str,input().split())
arr=[]
n=len(s)
for i in range(1,n+1):
    arr.append(s[-i:])
arr.sort()
print(arr[int(k)-1])