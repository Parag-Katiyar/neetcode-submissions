# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Count the number of nodes in the list
        cur = head
        count = 0
        while cur and count < k:
            cur = cur.next
            count += 1
        
        # If we have k nodes, reverse them
        if count == k:
            # Reverse k nodes
            reversed_head = self.reverse(head, k)
            # Recurse for the remaining list and connect
            head.next = self.reverseKGroup(cur, k)
            return reversed_head
        
        # If fewer than k nodes, return head as is
        return head

    def reverse(self, head: ListNode, k: int) -> ListNode:
        prev = None
        cur = head
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
