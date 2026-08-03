# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def compare(node, root):
    if node == None and root != None: 
        return False 
    if node != None and root == None: 
        return False 
    if node == None and root == None: 
        return True

    if node.val == root.val: 
        if compare(node.right, root.right) and compare(node.left, root.left):
            return True
    if node.val != root.val: 
        return False 

    return False


def find (node, root):

    if node == None: 
        return False 
    


    if compare(node, root):
        return True
    
    return find(node.left, root) or find(node.right, root)
   

    return False 


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return find(root,subRoot)



        