def checkIfExist(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] == arr[j] * 2 and j != i:
                return True
    return False
arr=[1,2,3,4,5]
print(checkIfExist(arr))