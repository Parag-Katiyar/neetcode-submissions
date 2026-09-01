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

        rmap = {}

        if head is None: 
            return None

        head_new  = Node(head.val)
        curr_new = head_new 

        rmap[head] = [curr_new]


        curr_old = head.next


        while curr_old != None: 

          new_node = Node(curr_old.val)

          rmap[curr_old] = [new_node]

          curr_new.next = new_node

          curr_new = new_node

          curr_old = curr_old.next

        for x in rmap: 

            if x.random is None: 
                rmap[x][0].random = None 
            else: 
                rmap[x][0].random = rmap[x.random][0]


        return head_new

        