from pyparsing import Optional


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node


class Solution:
    def addTwoNum(self, l1, l2):
        carry = 0
        resultList = ListNode()
        temp = l1.val + l2.val + carry
        carry = 1 if temp > 9 else 0
        resultList.val = temp % 10
        resultList.next = self.addTwoNum(l1.next, l2.next)
        return resultList



def __main__():
    first = LinkedList()
    second = LinkedList()

    first.push(3)
    first.push(4)
    first.push(2)

    second.push(4)
    second.push(6)
    second.push(5)

    result = Solution().addTwoNum(first.head, second.head)
    print(result)
