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