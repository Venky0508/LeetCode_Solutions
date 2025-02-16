# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        node_vals = []
        dfs(root, node_vals)
        
        if len(node_vals) == 1:
            return False
        
        node_vals.sort()

        i = 0
        j = len(node_vals) - 1

        while i < j:
            if node_vals[i] + node_vals[j] == k:
                return True
            elif node_vals[i] + node_vals[j] > k:
                j -= 1
            else:
                i += 1

        return False

def dfs(node, values):
    if node is not None:
        values.append(node.val)
        dfs(node.left, values)
        dfs(node.right, values)