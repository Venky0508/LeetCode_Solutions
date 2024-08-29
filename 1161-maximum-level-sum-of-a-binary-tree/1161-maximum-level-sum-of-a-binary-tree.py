# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # if root == None:
        #     return 0

        # max_sum = float("-inf")
        # max_level = 0
        # current_level = 0

        # q = deque([root])
        
        # while q:
        #     current_level += 1
        #     current_level_sum = 0
    
        #     for _ in range(len(q)):
        #         current_node = q.popleft()
        #         current_level_sum += current_node.val

        #         if current_node.left: 
        #             q.append(current_node.left)
        #         if current_node.right: 
        #             q.append(current_node.right)

        #     if current_level_sum > max_sum:
        #         max_sum = current_level_sum
        #         max_level = current_level
            
        # return  max_level

        if root == None:
            return 0
        
        level = 1
        storage = {}
        maxSum(root, level, storage)
        maxLevel = 0
        maxVal = float('-inf')
        for k , v in storage.items():
            print(f"{k} : {v}")
            if v > maxVal:
                maxVal = v
                maxLevel = k

        return maxLevel



def maxSum(node, level, store):
    if node != None:
        if level not in store:
            store[level] = node.val
            maxSum(node.left, level+1, store)
            maxSum(node.right, level+1, store)
        else:
            store[level] += node.val
            maxSum(node.left, level+1, store)
            maxSum(node.right, level+1, store)

        