'''
https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
'''
def repeatedString(s, n):
    x=n//len(s)
    ca=s.count('a')
    c1=x*ca
    str2=s[:n%len(s)]
    c2=str2.count('a')
    return c1+c2
print(repeatedString('aba',10))