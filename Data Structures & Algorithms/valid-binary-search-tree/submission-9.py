# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def valid(node, lower, upper):
    if node is None:
        return True

    if lower is not None and node.val <= lower:
        return False

    if upper is not None and node.val >= upper:
        return False

    return (valid(node.left, lower, node.val) and valid(node.right, node.val, upper))




class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return valid(root, None, None)


        