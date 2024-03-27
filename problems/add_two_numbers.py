# Definition for single linked list
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1, l2):

        carry = 0
        resultList = ListNode()
        temp = l1.val + l2.val
        carry = 1 if (temp>9) else 0
        resultList.val = temp%10
        
        if l1.next or l2.next:

            resultList.next = self.addTwoNumbers(l1.next, l2.next)
            resultList.next.val +=carry
        return resultList




l1 = [2, 4, 3]
l2 = [5, 6, 4]
l13 = ListNode(val=3, next=None)
l12 = ListNode(val=4, next=l13)
l11 = ListNode(val=2, next=l12)

l23 = ListNode(val=4, next=None)
l22 = ListNode(val=6, next=l23)
l21 = ListNode(val=5, next=l22)

s = Solution()
s1 = s.addTwoNumbers(l11, l21)
while s1.next:
    print(s1.val)
    s1 = s1.next
print(s1.val)



