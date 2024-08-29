class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i = 0
        j = len(nums) - 1
        count = 0
        nums.sort()

        while j > i:
            val1 = nums[i]
            val2 = nums[j]
            total = val1 + val2

            if total == k:
                count += 1
                i += 1
                j -= 1
            
            if total < k:
                i += 1
            
            if total > k:
                j -= 1

        return count


        