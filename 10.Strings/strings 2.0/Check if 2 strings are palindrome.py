from collections import Counter
def isPalindrome(str1,str2):
    return len(str1)==len(str2) and Counter(str1)==Counter(str2)
str1="chdan"
str2="nadnc"
print(isPalindrome(str1,str2))