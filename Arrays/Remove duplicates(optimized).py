def RemoveDup(nums):
    if len(nums) < 1:
        return len(nums)
    i = 0
    j = i + 1
    while j < len(nums):
        if nums[j] == nums[i]:
            j += 1
        else:
            nums[i + 1] = nums[j]
            i += 1
    return nums[:i+1]

nums=[1,2,2,3,3,3,4,5,5]
print(RemoveDup(nums))
