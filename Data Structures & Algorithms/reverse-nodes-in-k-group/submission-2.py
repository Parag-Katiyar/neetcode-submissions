# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(start_node, k):
    # Check if there are at least k nodes available to reverse
    count_step = 0 
    curr_x = start_node  # FIX: Start checking from start_node directly

    while count_step != k: 
        if curr_x is None: 
            return 0
        curr_x = curr_x.next
        count_step = count_step + 1
    
    # FIX: Standard independent list reversal logic for k nodes to prevent circular loops
    pre = None
    curr = start_node
    count_step = 0 

    while count_step < k: 
        t = curr.next 
        curr.next = pre 
        pre = curr 
        curr = t 
        count_step = count_step + 1 
    
    # pre is the new group head, curr is the start of the next unreversed group
    return pre, curr
    

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        do = 0
        curr = head
        last_cycle_end = None

        while curr:
            # FIX: Changed 'if' to 'elif' blocks to ensure only ONE state executes per loop pass
            if do == 0:
                result = reverse(curr, k) 

                if result == 0: 
                    return head
                
                end, new_start = result
                
                head = end 
                curr.next = new_start
                last_cycle_end = curr 
                curr = new_start 

                do = 1

            elif do == 2:
                result = reverse(curr, k) 

                if result == 0: 
                    return head
                
                end, new_start = result
                
                last_cycle_end.next = end
                curr.next = new_start

                last_cycle_end = curr
                curr = new_start

                do = 1
                
            elif do == 1:
                # FIX: Removed the 'for i in range(0, k-1)' loop.
                # Your 'reverse' function already advanced 'curr' to 'new_start' perfectly.
                # All we need to do here is transition back to state 2.
                do = 2 
                
        return head 
