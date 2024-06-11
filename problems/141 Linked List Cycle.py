# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        fast_hare = slow_tortoise = head

        while fast_hare and fast_hare.next:
            head = head.next
            fast_hare = fast_hare.next.next

            if fast_hare == head:
                return True
        
        return False

        ## set way of doing it
         
        # if head is None:
        #     return False

        # l = set()

        # while head.next:
        #     if head in l:
        #         return True
        #     else:
        #         l.add(head)
        #         head = head.next
        
        # return False
            
