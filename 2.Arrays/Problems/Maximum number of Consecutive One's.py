'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

'''
def findMaxConsecutiveOnes(nums):
    count = 0
    result = 0
    n=len(nums)
    for i in range(0, n):
        if (nums[i] == 0):
           count = 0
        else:
            count+= 1
            result = max(result, count)
    return result


n = int(input("Enter number of elements:"))
items = []
for _ in range(n):
    item = int(input("Enter the binary Elements:"))
    items.append(item)
print(findMaxConsecutiveOnes(items))
