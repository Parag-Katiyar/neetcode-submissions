# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None or head.next == None or (head.next).next == None:
            return False 

        x = head

        s = set()

        while x not in s:

            s.add(x)
            x = x.next
            if x == None: 
                return False 
        
        return True 







        
        