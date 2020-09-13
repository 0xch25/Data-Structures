'''
Impementation of Shell sort
References:https://www.geeksforgeeks.org/shellsort/
'''
def shellsort(lst):
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst

lst=[]
n=int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(n):
    x=int(input())
    lst.append(x)
print("Sorted elements:",shellsort(lst))