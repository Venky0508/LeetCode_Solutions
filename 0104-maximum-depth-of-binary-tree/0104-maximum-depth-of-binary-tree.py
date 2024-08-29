# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        counts = []
        countNodes(root, 1, counts)
        return max(counts)

def countNodes(node, count, counts):
    if node.left is not None:
        countNodes(node.left, count+1, counts)
    if node.right is not None:
        countNodes(node.right, count+1, counts)
    if node is not None:
        counts.append(count)
    