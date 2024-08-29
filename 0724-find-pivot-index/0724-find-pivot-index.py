class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums) - nums[0]
        temp = sum(nums) - nums[-1]
        prev = 0
        for i in range(len(nums)):
            if i == 0:
                left = 0
                if left == right:
                    return i
            elif i == len(nums) - 1:
                left = temp
                right = 0
                if left == right:
                    return i     
            else:
                left = prev + nums[i - 1]
                right -= nums[i]
                prev = left
                if left == right:
                    return i

        return -1




        