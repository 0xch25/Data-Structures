'''
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).



Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array
'''
nums = [3,4,2,3]
def numdec(nums):
    modified = False
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            if modified:
                return False
            if i >= 2 and nums[i] < nums[i - 2]:
                nums[i] = nums[i - 1]
            modified = True
    return True
print(numdec(nums))