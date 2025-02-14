class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # countArr = [0, 0]

        # for i in nums:
        #     countArr[i] += 1

        # maxLength = min(countArr[0], countArr[1])
        # return (2 * maxLength)
        n = len(nums)
        
        
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
       
        
        map = {}
        sum = 0
        ans = 0
        
        for i in range(n):
            sum += nums[i]

            if sum == 0:
                ans = i + 1

            if sum in map:
                length = i - map[sum]
                ans = max(length, ans)
            else:
                map[sum] = i
        
        return ans
        