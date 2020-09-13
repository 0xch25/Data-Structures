'''
Implementation of Insertion sort
'''

def insort(lst):
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = key

lst=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    x=int(input())
    lst.append(x)
insort(lst)
print("Sorted Array:")
print(lst)