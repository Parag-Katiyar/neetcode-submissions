# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invert(node): 

    if node == None: 
        return 

    r = node.right
    l = node.left

    node.right = l 
    node.left = r    

    invert(node.right)
    invert(node.left)
   

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None: 
            return root 
        
        invert(root)
        return root
        