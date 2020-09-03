'''
Write a Function to find the node at which the intersection of two singly linked lists begins
Approach1:using Dictionaries

def getIntersectionNode(headA,headB):
    dict = {}
    while headA:
        dict[headA] = 1
        headA = headA.next
    while headB:
        if headB in dict:
            return headB
        headB = headB.next
    return None

'''
#Approach2:Optimized Version

    def getIntersectionNode1(headA,headB):
        tempA = headA
        lenA = 0
        while (tempA):
            lenA += 1
            tempA = tempA.next

        tempB = headB
        lenB = 0
        while (tempB):
            lenB += 1
            tempB = tempB.next

        if lenA > lenB:
            while (lenA != lenB):
                headA = headA.next
                lenA -= 1
        if lenA < lenB:
            while (lenA != lenB):
                headB = headB.next
                lenB -= 1

        while (headA and headB):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None