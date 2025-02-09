class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        aux = set()
        for i in nums:
            aux.add(i)
        if len(nums) != len(aux):
            return True
        return False

        


