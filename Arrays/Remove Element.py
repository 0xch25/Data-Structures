def removeElement(nums,val):
    while val in nums:
        nums.remove(val)
    return len(nums)
nums=[1,2,3,3,4,3]
val=3
removeElement(nums,val)
print(nums)