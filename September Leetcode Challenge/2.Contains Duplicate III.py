'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false

'''


def dup3(nums,k,t):
    if t == 0:
        if len(nums) == len(set(nums)):
            return False
        return True
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if abs(nums[j] - nums[i]) <= t and i != j and abs(j - i) <= k:
                return True
    return False
nums = [1,0,1,1]
k = 1
t = 2
print(dup3(nums,k,t))
nums = [1,5,9,1,5,9]
k = 2
t = 3
print(dup3(nums,k,t))