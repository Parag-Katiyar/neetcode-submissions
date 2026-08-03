# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def same(node1, node2):
    
    if node1 == None and node2 == None:
        return True 
    
    if node1 != None and node2 == None:
        return False

    if node1 == None and node2 != None:
        return False 

    if node1.val != node2.val:
        return False
    
    if same(node1.right,node2.right) and same(node1.left, node2.left):
        return True 

    return False

    

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        return same(p,q)







        