'''
check the given string has all unique letters.
(without using additional data structures)
'''
#Brute force method: O(n^2)

def isUnique(str):
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if str[i]==str[j]:
                return False
    return True

#using sort:O(n log n)
def isUnique2(str):
    str = sorted(str)
    for i in range(len(str) - 1):
        if str[i] == str[i + 1]:
            return False
    return True


str = "handc"
print(isUnique(str))
print(isUnique2(str))


