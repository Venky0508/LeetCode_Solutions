class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums != []:
            k = k % len(nums)
            temp = nums[-k:] + nums[:-k]
            for i in range(len(nums)):
                nums[i] = temp[i]
      
                
        