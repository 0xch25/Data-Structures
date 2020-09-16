'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.
Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
'''


def smallerNumbersThanCurrent(nums):
    res = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[j] < nums[i]:
                count += 1
        res.append(count)
    return res
nums=[8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))

'''
Approach 2(Hashing)
        
        d={}
        snums=sorted(nums)
        for i,v in enumerate(snums):
            if v not in d:
                d[v]=i
        return [d[n] for n in nums]
'''