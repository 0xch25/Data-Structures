'''Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.'''

# ****OPTIMIZED****
def sortArrayByParityV1(A):
    return [s for s in A if s%2==0]+[s for s in A if s%2!=0]

#Basic
def sortArrayByParity(A):
    B = []
    for num in A:
        if num % 2 == 0:
            B.insert(0, num)
        else:
            B.insert(len(A) - 1, num)
    return B
#using in-place Array Operations and Lambda function
def sortArrayByParityV2(A):
        A.sort(key=lambda x: x % 2)
        return A

A=[1,2,3,4]
print(sortArrayByParity(A))
print(sortArrayByParityV2(A))
print(sortArrayByParityV1(A))