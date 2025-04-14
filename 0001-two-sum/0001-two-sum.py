class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # arr = list(nums)
        # arr.sort()

        # i = 0
        # j = len(arr) - 1
        # x = 0
        # y = 0
        # while i < j:
        #     if arr[i] + arr[j] == target:
        #         x = arr[i]
        #         y = arr[j]
        #         break

        #     elif arr[i] + arr[j] > target:
        #         j -= 1

        #     else:
        #         i += 1

        # a = nums.index(x)
        # nums[a] = float('inf')
        # b = nums.index(y)
        # return [a,b]

        numMap = dict()

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in numMap:
                return[numMap[diff],i]
            
            numMap[nums[i]] = i

        
