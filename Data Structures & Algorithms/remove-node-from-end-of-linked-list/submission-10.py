# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None: 
            return 
        
        fast = head 
        slow = head
        a = 0 
       

        while fast != None: 
             
            fast = fast.next
            a = a + 1 

            if a > n+1: # a > n is the right condition  in this steup 

                
                slow = slow.next
                
        if  a == n : 
            return head.next

        if  a != n:
            slow.next = slow.next.next

            return head


