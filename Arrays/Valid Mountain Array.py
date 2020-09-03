'''
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
                    A[0] < A[1] < ... A[i-1] < A[i]
                    A[i] > A[i+1] > ... > A[A.length - 1]
Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
'''
def validMountainArray(A):
    if len(A) < 3 or sorted(A) == A:
        return False

    else:
        max_index = A.index(max(A))
        if max_index != 0 and max_index != len(A):
            for i in range(0, max_index):
                if A[i] >= A[i + 1]:
                    return False
            else:
                for j in range(max_index, len(A) - 1):
                    if A[j] <= A[j + 1]:
                        return False
                else:
                    return True
        else:
            return False
A=[0,1,2,3,2,1]
B=[1,2,3,1,2,3]
print(validMountainArray(A))
print(validMountainArray(B))