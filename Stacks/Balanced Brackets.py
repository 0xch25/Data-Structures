'''program to check the given string is balanced or not using staks'''
def isMatch(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    else:
        return False


def isBalanced(str):
    stk = []
    balanced = True
    index = 0
    while index < len(str) and balanced:
        paren = str[index]
        if paren in "[{(":
            stk.append(paren)
        else:
            if stk == []:
                balanced = False
            else:
                top = stk.pop()
                if not isMatch(top, paren):
                    balanced = False
        index += 1
    if balanced:
        return "Yess..its balanced :)"
    return "Nope :("


str1 = "({[]})"
str2 = "({[})"
str3="{}{}[]"
print(isBalanced(str1))
print(isBalanced(str2))
print(isBalanced(str3))