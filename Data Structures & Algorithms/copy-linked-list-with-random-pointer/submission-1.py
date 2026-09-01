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

        rmap[head] = [head.random,curr_new]


        curr_old = head.next


        while curr_old != None: 

          new_node = Node(curr_old.val)

          rmap[curr_old] = [curr_old.random,new_node]

          curr_new.next = new_node

          curr_new = new_node

          curr_old = curr_old.next

        for x in rmap: 

            if rmap[x][0] is None: 
                rmap[x][1].random = None 
            else: 
                rmap[x][1].random = rmap[rmap[x][0]][1]


        return head_new


          




          














        
        