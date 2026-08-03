# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Edge Case empty list and single element list 
        if head == None: 
            return 

        if head.next == None and n > 0: 
            return None 
        
        fast = head 
        slow = head
        a = 0 
        pre = None

        while fast != None: 
             
            fast = fast.next
            a = a + 1 

            if a > n:

                pre = slow
                slow = slow.next
                

            if fast == None: 

                if pre == None :  
                    return head.next
                else: 
                    pre.next = slow.next

                return head

                
               

        
             












        