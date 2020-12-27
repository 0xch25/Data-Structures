def twosum(array,tar):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i]+array[j]==tar:
                return i,j
'''
    dict={}
    for i in range(len(array)):
        dict[i] = array[i]
    for i in range(len(array)-1):
        if(dict[i] + dict[i+1])==tar:
            print(i,i+1)
'''




array=list(map(int,input().split()))
tar=int(input("enter the target number:"))
print(twosum(array,tar))