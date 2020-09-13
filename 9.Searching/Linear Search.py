'''
Implementation of Linear Search in Python3

'''
def linearsearch(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            print("Element Found")
            return
    print("Element Not Found")
arr=[10,20,14,45,78,9,8,62,321,458]
x=int(input("Enter the Element to find:"))
linearsearch(arr,x)