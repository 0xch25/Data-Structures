'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.
'''
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
