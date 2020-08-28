def findMaxConsecutiveOnes(nums):
    count = 0
    result = 0
    n=len(nums)
    for i in range(0, n):
        if (nums[i] == 0):
           count = 0
        else:
            count+= 1
            result = max(result, count)
    return result


n = int(input("Enter number of elements"))
items = []
for _ in range(n):
    item = int(input("Enter the binary Elements"))
    items.append(item)
print(findMaxConsecutiveOnes(items))
