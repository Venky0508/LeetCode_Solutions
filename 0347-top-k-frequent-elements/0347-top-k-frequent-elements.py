class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums)
        nums = set(sorted_nums)
        count_arr = []
        
        for i in nums:
            j = sorted_nums.count(i)
            count_arr.append((i,j))
            
        count_arr = sorted(count_arr, key = lambda x:x[1])
        res = []
        index = len(count_arr) - 1
        for _ in range(k):
            res.append(count_arr[index][0])
            if index - 1 >= 0:
                index -= 1
        
        return res