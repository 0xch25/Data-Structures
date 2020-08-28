def findNumbers(nums):
    count = 0
    for num in nums:
        s = len(str(num))
        if s % 2 == 0:
            count += 1
    return count
nums=[12,123,1234,11111,1]
print(findNumbers(nums))