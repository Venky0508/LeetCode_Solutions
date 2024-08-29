class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # n = len(nums)

        # for i in range(n):
        #     one = nums[i]
        #     for j in range(i+1, n):
        #         two = nums[j]
        #         if one < two:
        #             for k in range(j+1, n):
        #                 three = nums[k]
        #                 if two < three:
        #                     return True
        

        # return False

        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')

        
        for n in nums:
            if n <= first:
                first = n  
            elif n <= second:
                second = n  
            else:
                return True  
        
        return False
                
            
