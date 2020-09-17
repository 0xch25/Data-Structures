'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
'''
def diagonalDifference(arr):
    a=[]
    b=[]
    for i in range(len(arr)):
        a.append(arr[i][i])
    for i in range(len(arr)):
        b.append(arr[i][len(arr)-1-i])
    return (abs(sum(a)-sum(b)))
arr=[[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(arr))