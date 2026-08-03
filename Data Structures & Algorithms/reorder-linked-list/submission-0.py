# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #Edge case of Null list or single or double list 

        if head == None or head.next == None or head.next.next == None: 
            return 
    
        # Finding Half
        slow = head 
        fast = head

 
        while fast.next!=None and fast.next.next != None:
            slow = slow.next 
            fast = (fast.next).next

        half = slow.next 
        slow.next = None 

        #Reversing the second half of the list 
        pre = None 
        curr = half

        while curr != None:
            next = curr.next 
            curr.next = pre 
            pre = curr 
            curr = next 
        
        last = pre
        start = head 

        #Creating the final list 
        #head and last 
        while last and start: 
            s1 = start.next 
            s2 = last.next
            start.next = last 
            last.next = s1
            start = s1
            last = s2
        

        
        








       









       