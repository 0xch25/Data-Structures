'''promgram to implement getMin function which takes O(1) using 2 stacks'''
stk=[]
minstk=[]
class Stack:
    def push(self,data):
        if len(stk)==0 and len(minstk)==0:
            minstk.append(data)
            stk.append(data)

        else:
            if data<minstk[0]:
                stk.append(data)
                minstk.append(data)
            else:
                stk.append(data)
    def pop(self):
        x=stk.pop()
        minstk.pop()
        return x
    def getMin(self):
        return minstk[-1]
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.getMin())
s.push(5)
print(s.getMin())
s.pop()
print(s.getMin())