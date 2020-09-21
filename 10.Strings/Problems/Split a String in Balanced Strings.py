'''
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.



Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'
'''


def balancedStringSplit(s):
    res = count = 0
    for c in s:
        if c == 'L':
            count += 1
        if c == 'R':
            count -= 1
        if count == 0:
            res += 1
    return res
s = "RLRRLLRLRL"
print(balancedStringSplit(s))