# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return None
        
#         maxLength = 0
#         if root.left:
#             zigzag(root.left, maxLength, 2, 'left')
#         if root.right:
#             zigzag(root.right, maxLength, 2, 'right')
        
#         print(lengths)
#         return max(lengths)
            

            
# def zigzag(node, lengths, count, curr):
#     if node != None:
#         if curr == 'left':
#             zigzag(node.right, lengths, count+1, 'right')
#             zigzag(node.left, lengths.append(count - 1), 2, 'left')
#         else:
#             zigzag(node.left, lengths, count+1, 'left')
#             zigzag(node.right, lengths.append(count - 1), 2, 'right')


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.pathLengths = []
        
        def dfs(node, goLeft, steps):
            if node:
                self.pathLengths.append(steps)
                if goLeft:
                    dfs(node.left, False, steps + 1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, steps + 1)
        
        dfs(root, False, 0)
        dfs(root, True, 0)
        return max(self.pathLengths)