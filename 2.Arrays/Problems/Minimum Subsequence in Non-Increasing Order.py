'''
https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
'''


def minSubsequence(nums):
    nums.sort()
    res = [nums.pop()]
    while sum(res) <= sum(nums):
        res.append(nums.pop())
    return res
nums = [4,3,10,9,8]
print(minSubsequence(nums))