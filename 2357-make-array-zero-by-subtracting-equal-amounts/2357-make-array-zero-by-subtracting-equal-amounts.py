class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return 0
        
        nums.sort()
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            
            else:
                count += 1
                val = nums[i]
                nums[i] = 0
                
                if i+1 < len(nums):
                    for j in range(i+1, len(nums)):
                        nums[j] -= val

                if sum(nums) == 0:
                    return count