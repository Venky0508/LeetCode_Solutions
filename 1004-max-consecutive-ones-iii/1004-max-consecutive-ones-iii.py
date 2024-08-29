class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # maxCount = 0
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] == 0:
        #         if k >= 1:
        #             zeroSeen = 1
        #             j = i + 1
        #             count = 1
        #             while j < n and zeroSeen <= k:
        #                 if nums[j] == 1:
        #                     count += 1
        #                     j += 1
        #                 elif nums[j] == 0:
        #                     if zeroSeen == k:
        #                         break
        #                     count += 1
        #                     zeroSeen += 1
        #                     j += 1

        #             if count > maxCount:
        #                 maxCount = count
        #         else:
        #             continue
            
        #     elif nums[i] == 1:
        #         zeroSeen = 0
        #         j = i + 1
        #         count = 1

        #         while j < n and zeroSeen <= k:
        #             if nums[j] == 1:
        #                 count += 1
        #                 j += 1
        #             elif nums[j] == 0:
        #                 if zeroSeen == k:
        #                     break
        #                 count += 1
        #                 zeroSeen += 1
        #                 j += 1

        #         if count > maxCount:
        #             maxCount = count
        
        # return maxCount

        n = 0
        left = 0
        zeros_count = 0

        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1
            
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            
            n = max(n, right - left + 1)

        return n



        