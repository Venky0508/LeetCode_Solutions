# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root.val == p.val or root.val == q.val:
            return root

        return lca(root, p, q)
        

def lca(root, p, q):
    if root is None or root.val == p.val or root.val == q.val:
            return root
    l = lca(root.left, p, q)
    r = lca(root.right, p, q)

    if l != None and r != None:
        return root
    elif l == None:
        return r
    else:
        return l
    

        