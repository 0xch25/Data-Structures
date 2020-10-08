'''
find the missing number in the given array:
input:
4
1 2 4
output:3
'''
def missing_nums(n,nums):
    nums2=[]
    for i in range(1,n+1):
        nums2.append(i)
    return sum(nums2)-sum(nums)
nums=[]
n=int(input("Enter the number of elements:"))
for j in range(n-1):
    x=int(input())
    nums.append(x)
print("missing number is:",missing_nums(n,nums))