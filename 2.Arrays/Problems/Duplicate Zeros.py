'''
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.
Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

'''
def duplicateZeros(arr):
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] == 0:
            arr.insert(i + 1, 0)
            arr.pop()
            i += 2
        else:
            i += 1
    return arr
arr=[0,1,2,0,0,0,8]
print(duplicateZeros(arr))
'''
OUTPUT:
[0, 0, 1, 2, 0, 0, 0]
'''