'''
Given an array nums of integers, return how many of them contain an even number of digits.
 Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
'''
def findNumbers(nums):
    count = 0
    for num in nums:
        s = len(str(num))
        if s % 2 == 0:
            count += 1
    return count
nums=[12,123,1234,11111,1]
print(findNumbers(nums))