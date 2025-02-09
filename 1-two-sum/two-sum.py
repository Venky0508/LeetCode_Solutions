class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         i = 0
#         j = len(nums) - 1
#         x = 0
#         y = len(nums) - 1
        
        
#         while i < j and x < y:
#             one = nums[i]
#             two = nums[j]
#             three = nums[x]
#             four = nums[y]
#             total1 = one + two
#             total2 = three + four
#             if total1 > target :
#                 j -= 1
#             elif total1 < target:
#                 i += 1
#             elif total1 == target:
#                 return [i, j]
#             if total2 > target :
#                 x += 1
#             elif total2 < target:
#                 y -= 1
#             else:
#                 return [x, y]
        
#         return []
            
        for y in range(0, len(nums)) :
            for z in range(y+1, len(nums)):
                if nums[y] + nums[z] == target: 
                    return [y , z]
        