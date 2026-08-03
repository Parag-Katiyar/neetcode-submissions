# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(x, pre1):
            s = x.next
            x.next = pre1
            pre1 = x
            x = s
            if x== None: 
                return pre1
            else: 
                return reverse(x,pre1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head
        
        curr = head.next 
        head.next = None 
        pre = head

        pre = reverse(curr,pre)

        return pre

        
        