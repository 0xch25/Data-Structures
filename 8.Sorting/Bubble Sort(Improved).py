'''
Implementation of Modified Bubble sort.

'''
def Bubblesort(lst):
    for i in range(n-1):
        swapped=False
        for k in range(n-i-1):
            if lst[k]>lst[k+1]:
                temp=lst[k]
                lst[k]=lst[k+1]
                lst[k+1]=temp
                swapped=True
        if swapped==False:
            break
    return lst

n=int(input("Enter The No of Elements:"))
lst=[]
print("Enter The Elements:")
for _ in range(n):
    x=int(input())
    lst.append(x)
print("The Sorted Elements are:",Bubblesort(lst))