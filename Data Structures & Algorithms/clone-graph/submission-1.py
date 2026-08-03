"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
def clone (node,clone_map):
    
    if node in clone_map: 
        return clone_map[node]

    clone_map[node] = Node(node.val)

    for neighbour in node.neighbors: 
        clone_map[node].neighbors.append(clone(neighbour,clone_map))
    
    return clone_map[node]


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node == None: 
            return None

        clone_map = {}
        return clone (node,clone_map)
        
        

        













        




        