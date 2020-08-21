'''Program to check weather the given string is palindrome or not (without using Stacks)'''
def palindrome(str):
    n = len(str) - 1
    x = int(n / 2)
    str1 = str[0:x]
    print("first half:", str1)
    str2 = str[:x:-1]
    print("second half:", str2)
    if str1 == str2:
        print("palindrome")
    else:
        print("not palindrome")


palindrome("abababbbabbXabbbabbabbb")  # Not palindrome
palindrome("ababXbaba") #palindrome
