arr=[]
n=int(input())
for _ in range(n):
    arr.append(input())
for i in range(n):
    count=0
    for j in range(0,i):
        if arr[j]<arr[i]:
            count+=1
    print(count)