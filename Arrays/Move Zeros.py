'''Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
One Line Solutuon: nums.sort(key=lambda x: x == 0)
'''
def moveZeroes(nums):
    count = 0
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            nums.remove(nums[i])
            count += 1
    for i in range(count):
        nums.append(0)

nums=[0,1,0,3,12]
moveZeroes(nums)
print(nums)