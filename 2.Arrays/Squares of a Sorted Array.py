'''Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
One Line Solution:
                     def sortedSquares(self, A: List[int]) -> List[int]:
                        return sorted([x**2 for x in A])

'''
def sortedSquares(A):
    B = []
    for i in A:
        B.append(i * i)
    return sorted(B)
A=[1,2,3,21,0]
print(sortedSquares(A))