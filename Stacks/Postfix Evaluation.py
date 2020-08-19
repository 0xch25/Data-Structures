def postfix_evaluation(str):
    s=str.split()
    n=len(s)
    stack =[]
    for i in range(n):
        if s[i].isdigit():
            stack.append(int(s[i]))
        elif s[i]=="+":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(a)+int(b))
        elif s[i]=="*":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(a)*int(b))
        elif s[i]=="/":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(b)/int(a))
        elif s[i]=="-":
            a=stack.pop()
            b=stack.pop()
            stack.append(int(b)-int(a))
    return stack.pop()

str="100 200 + 2 / 5 * 7 +"
str2="2 3 1 * + 9 -"

print(postfix_evaluation(str))
print(postfix_evaluation(str2))