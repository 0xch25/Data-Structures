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