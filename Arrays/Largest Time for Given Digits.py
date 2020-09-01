'''Given an array of 4 digits, return the largest 24 hour time that can be made.
The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
Return the answer as a string of length 5.  If no valid time can be made, return an empty string.
Example 1:
Input: [1,2,3,4]
Output: "23:41"
Example 2:
Input: [5,5,5,5]
Output: ""
'''
import itertools
def largestTimeFromDigits(A):
    return max(("%d%d:%d%d" % time for time in itertools.permutations(A) if time[:2] < (2, 4) and time[2] < 6), default="")

A=[1,2,3,4]
B=[5,5,5,5]
print(largestTimeFromDigits(A))
print(largestTimeFromDigits(B))