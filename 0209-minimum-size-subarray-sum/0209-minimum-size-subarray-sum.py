class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         if sum(nums) < target:
#             return 0
        
        
#         left = 0
#         right = 0
#         ans = float('inf')
        
#         while right <= len(nums):
#             temp = sum(nums[left:right])
#             if temp < target:
#                 right += 1
#             else:
#                 left += 1
#                 if right -left + 1 < ans:
#                     ans = right - left + 1
        
#         if ans == float('inf'):
#             return 0
        
#         return ans
        left = 0
        right = 0
        sumOfCurrentWindow = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sumOfCurrentWindow += nums[right]

            while sumOfCurrentWindow >= target:
                res = min(res, right - left + 1)
                sumOfCurrentWindow -= nums[left]
                left += 1

        return res if res != float('inf') else 0