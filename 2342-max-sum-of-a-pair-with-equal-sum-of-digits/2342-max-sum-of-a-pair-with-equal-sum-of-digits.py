class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        num_map = {}
        # nums = [229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401]
        for i in nums:
            total = 0
            temp = i
            while temp > 0:
                total += (temp % 10)
                temp //= 10
            
            if total not in num_map:
                num_map[total] = [i]
            else:
                num_map[total].append(i)

        maxSum = -1

        for k,v in num_map.items():
            if len(v) > 1:
                v.sort(reverse = True)
                if v[0] + v[1] > maxSum:
                    maxSum = v[0] + v[1]

        return maxSum
