'''
https://www.hackerrank.com/challenges/staircase/problem?h_r=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_r%5B%5D%5B%5D=next-challenge&h_v=zen&h_v%5B%5D%5B%5D=zen&h_v%5B%5D%5B%5D=zen&isFullScreen=true&h_r=next-challenge&h_v=zen

'''
def staircase(n):
    for i in range(1, n + 1):
       print(' ' * (n - i) + '#' * i)
n=7
staircase(n)