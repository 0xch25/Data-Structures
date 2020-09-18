'''
https://www.hackerrank.com/challenges/birthday-cake-candles/problem
'''
def birthdayCakeCandles(candles):
    return candles.count(max(candles))
candles=[1,2,4,3,4,4]
print(birthdayCakeCandles(candles))