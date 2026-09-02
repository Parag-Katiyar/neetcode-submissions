# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 is not None or l2 is not None or carry != 0:
            # Get values safely; use 0 if a list is exhausted
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Compute sum and new carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            new_digit = total_sum % 10
            
            # Append new node to our result list
            current.next = ListNode(new_digit)
            
            # Advance pointers
            current = current.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        return dummy_head.next
