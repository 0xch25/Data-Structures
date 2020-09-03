'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.
Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
'''
def replaceElements(arr):
    maxSoFar = arr[-1]
    arr[-1] = -1
    for i in range(len(arr) - 2, -1, -1):
        temp = arr[i]
        arr[i] = maxSoFar
        maxSoFar = max(maxSoFar, temp)
    return arr
arr = [17,18,5,4,6,1]
print(replaceElements(arr))