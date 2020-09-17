'''Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]'''
def runningSum(nums):
    sum =0
    for i in range(len(nums)):
        temp=nums[i]
        nums[i] =nums[i] +sum
        sum+=temp
    return nums

nums=[1,1,1,1,1]
nums2=[1,2,3,4]
print(runningSum(nums))
print(runningSum(nums2))