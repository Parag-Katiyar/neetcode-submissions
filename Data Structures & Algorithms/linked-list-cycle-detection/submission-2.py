# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
            
        slow = head
        fast = head
        
        # Fast pointer moves twice as fast as slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, there is a cycle
            if slow == fast:
                return True
                
        return False
        