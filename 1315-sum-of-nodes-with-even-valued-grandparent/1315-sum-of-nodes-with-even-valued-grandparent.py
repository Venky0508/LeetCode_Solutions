# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return dfs(root, 1, 1)



def dfs(root, dad, g_parent):
    if not root:
        return 0
    x = 0
    if g_parent % 2 == 0:
        x = root.val

    x += dfs(root.left, root.val, dad)
    x += dfs(root.right, root.val, dad)

    return x
            
        