class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result = set()
#         nums.sort()
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 one = nums[i]
#                 two = nums[j]
#                 temp = nums[:i] + nums[i+1:]
#                 temp = temp[:j-1] + temp[j:]
#                 total = (one + two) * -1
#                 if total in temp:
#                     triplet = (one, two, total)
#                     result.add(triplet)
        
#         return list(result)
        m=set()
        nums.sort()
        n=len(nums)
        for i in range(n):
            target=-1*nums[i]
            j=i+1
            k=n-1
            while(j<k):
                if nums[j]+nums[k]<target:
                    j+=1 
                elif nums[j]+nums[k]>target:
                    k-=1
                elif nums[j]+nums[k]==target:
                    m.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                        
                        
        return list(m)        
        