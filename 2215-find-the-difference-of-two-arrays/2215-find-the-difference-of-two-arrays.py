class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums2)
        set2 = set(nums1)

        ans = []
        new = set()

        for i in nums1:
            if i not in set1:
                new.add(i)
        
        ans.append(list(new))
        new = set()

        for j in nums2:
            if j not in set2:
                new.add(j)
        
        ans.append(list(new))
        return ans
        