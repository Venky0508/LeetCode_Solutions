# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or val is None:
            return None
        if root.val == val:
            return root

        return bsearch(root, val)

def bsearch(node, val):
    if node == None:
        return None
    elif node.val == val:
        return node
    elif node.val > val:
        return bsearch(node.left, val)
    else:
        return bsearch(node.right, val)
        