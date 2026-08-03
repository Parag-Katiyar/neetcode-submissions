# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invert(node): 


    r = node.right
    l = node.left

    node.right = l 
    node.left = r 

    if node.right and node.left:
        invert(node.left) 
        invert(node.right)


    if node.right!= None and node.left == None: 
        invert(node.right)
        return 

    if node.left != None and node.right == None: 
        invert(node.left)
        return 
    
    if node.left == None and node.right == None: 
        return
    
   


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None: 
            return root 
        

        invert(root)
        return root

        
        