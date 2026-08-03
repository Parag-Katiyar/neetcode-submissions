# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(x, pre1):

            
            netn = x.next
            x.next = pre1
           
            pre1 = x 
            
            if netn== None: 
                return pre1
            else: 
                return reverse(netn,pre1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head
        
        pre = reverse(head,None)

        return pre

        
        