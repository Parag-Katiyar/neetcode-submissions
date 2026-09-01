"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create all new nodes in a simple, short loop
        rmap = {}
        curr = head
        while curr:
            rmap[curr] = Node(curr.val)
            curr = curr.next
            
        # Step 2: Set both .next and .random in the second loop
        for x in rmap:
            if x.next:     rmap[x].next = rmap[x.next]
            if x.random:   rmap[x].random = rmap[x.random]
            
        return rmap[head]
