class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = float('-inf')
        left = 0
        right = k
        window = sum(nums[left:right])
        flag = 0
        while right < len(nums) or flag == 0:
            if flag == 0:
                average = window/k
                flag = 1
            else:
                rest = nums[right]
                rest -= nums[left]
                window += rest
                average = window/k
                left += 1
                right += 1
            
            if average > maxAvg:
                maxAvg = average
        
        return maxAvg
