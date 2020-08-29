def removeDuplicates(nums):
    nums[:] = list(dict.fromkeys(nums))
    return len(nums)

nums=[1,1,2,3,4,4,5,3,2]
removeDuplicates(nums)
print(nums)