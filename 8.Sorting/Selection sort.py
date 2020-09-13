'''
Implementation of Selection Sort
'''
def selsort(lst):
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if lst[min_index]>lst[j]:
                min_index=j
        lst[i],lst[min_index]=lst[min_index],lst[i]
    return lst
lst=[]
n=int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(n):
    x=int(input())
    lst.append(x)
print("Sorted elements:",selsort(lst))