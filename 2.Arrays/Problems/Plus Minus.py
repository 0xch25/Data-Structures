'''
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value

'''


def plusMinus(arr):
    l = len(arr)
    p = 0
    n = 0
    z = 0
    for i in range(l):
        if arr[i] > 0:
            p += 1
        elif arr[i] < 0:
            n += 1
        else:
            z += 1
    print(format(p / l, ".6f"))
    print(format(n / l, ".6f"))
    print(format(z / l, ".6f"))
arr=[-4,3,-9,0,4,1]
plusMinus(arr)