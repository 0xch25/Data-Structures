''' Third Maximum Number
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
Example 1:
Input: [3, 2, 1]
Output: 1
'''
def thirdMax(nums):
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    if len(nums) >=3:
        return nums[len(nums)-3]
    else:
        return max(nums)
nums=[3,2,1,4]
print(thirdMax(nums))