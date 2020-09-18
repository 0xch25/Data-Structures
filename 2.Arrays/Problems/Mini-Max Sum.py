'''
https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=false
'''
def miniMaxSum(arr):
    s=0
    for i in range(len(arr)):
        s+=arr[i]
    print(s-max(arr),s-min(arr))

arr=[1,2,3,4,5]
miniMaxSum(arr)
