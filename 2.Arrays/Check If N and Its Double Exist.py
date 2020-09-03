'''
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
'''
def checkIfExist(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] == arr[j] * 2 and j != i:
                return True
    return False
arr=[1,2,3,4,5]
print(checkIfExist(arr))