class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        counter = 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                counter += 1
            else:
                nums[i] = float('inf')

        nums.sort()
        return counter


