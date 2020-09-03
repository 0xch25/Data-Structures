'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]

'''
def merge(nums1,m, nums2, n):
    for i in range(n):
        nums1.pop()
    for n in nums2:
        nums1.append(n)
    nums1.sort()
nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
merge(nums1,m,nums2,n)
print(nums1)