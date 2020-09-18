'''
https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
'''
def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(n):
        for j in range(n):
            if i<j and ((ar[i]+ar[j])%k)==0:
                count+=1
    return count
n=6
k=3
ar=[1,3,2,6,1,2]
print(divisibleSumPairs(n,k,ar))