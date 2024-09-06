# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q:
            return False
        elif not q and p:
            return False
        elif not p and not q:
            return True
        else:
            return checkTree(p,q)
        
def checkTree(p,q):
    if not p and not q:
        return True
    if not p.left and q.left:
        return False
    elif not q.left and p.left:
        return False
    elif not p.right and q.right:
        return False
    elif not q.right and p.right:
        return False
    elif p.val != q.val:
        return False
    elif p.val == q.val:
        return checkTree(p.left, q.left) and checkTree(p.right, q.right)
