class Solution:
    def canJump(self, nums: List[int]) -> bool:
#         if len(nums) == 1:
#             return True
#         goal = len(nums) - 1
        
#         start = 0
#         stack = []
#         stack.append(0)
#         visited = set()
        
#         while stack != []:
#             index = stack.pop()
#             visited.add(index)
#             val = nums[index]
#             while val > 0:
#                 new = index + val
#                 if new == goal:
#                     return True
#                 if new not in visited:
#                     stack.append(new)
#                 val -= 1
#             stack.sort()
#             while stack != [] and stack[-1] in visited:
#                 stack.pop()
#                 if stack == []:
#                     break
        
#         return False
        
        reach = 0
        for i in range(len(nums)):
            if i > reach:
                return False  
            reach = max(reach,i+nums[i])
            
        return True