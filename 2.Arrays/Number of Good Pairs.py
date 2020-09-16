'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed
'''
class Solution:
    def numIdenticalPairs(self,nums):
        hashmap={}
        count=0
        for num in nums:
            if num in hashmap:
                count+=hashmap[num]
                hashmap[num]+=1
            else:
                hashmap[num]=1
        return count
s=Solution()
nums=[1,2,3,1,1,3]
print(s.numIdenticalPairs(nums))