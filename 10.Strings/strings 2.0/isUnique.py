'''
check the given string has all unique letters.
(without using additional data structures)
'''
#Naive method:

def isUnique(str):
    for i in range(len(str)):
        for j in range(i+1,len(str)):
            if str[i]==str[j]:
                return False
    return True
str="chandan"
print(isUnique(str))

