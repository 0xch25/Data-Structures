def replaceElements(arr):
    maxSoFar = arr[-1]
    arr[-1] = -1
    for i in range(len(arr) - 2, -1, -1):
        temp = arr[i]
        arr[i] = maxSoFar
        maxSoFar = max(maxSoFar, temp)
    return arr
arr = [17,18,5,4,6,1]
print(replaceElements(arr))