# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None: 
            return head
        
        curr = head.next
        head.next = None 
        pre = head 
        while curr != None: 
            s = curr.next 

            curr.next = pre 
            pre = curr 
            curr = s 
        head = pre 

        return head 






        
        