# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(start_node, k):

    pre = start_node
    curr = start_node.next

    # Check whether k nodes exist
    for _ in range(k - 1):

        if curr is None:
            return 0

        curr = curr.next

    # Reverse k nodes
    curr = start_node.next
    pre = start_node

    for _ in range(k - 1):

        t = curr.next
        curr.next = pre
        pre = curr
        curr = t

    # pre = new head of reversed group
    # curr = node after reversed group
    return pre, curr


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        prev_group = None
        new_head = None

        while curr:

            result = reverse(curr, k)

            # Less than k nodes remain
            if result == 0:
                break

            group_head, next_group = result

            # First group gives us the actual head
            if new_head is None:
                new_head = group_head
            else:
                # Connect previous reversed group
                prev_group.next = group_head

            # Original group head is now the tail
            curr.next = next_group

            # Save this group's tail
            prev_group = curr

            # Move to next group
            curr = next_group

        return new_head