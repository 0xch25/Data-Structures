def sortedSquares(A):
    B = []
    for i in A:
        B.append(i * i)
    return sorted(B)
A=[1,2,3,21,0]
print(sortedSquares(A))