class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
#         ans = 0
        
#         if arr1 == [] or arr2 == []:
#             return 0
        
#         for i in arr1:
#             for j in arr2:
#                 str1 = str(i)
#                 str2 = str(j)
#                 index = min(len(str1), len(str2))
#                 if str1[:index] == str2[:index] and index > ans:
#                         ans = index
        
#         return ans
        prefixes = set()
        for elem in arr2:
            while elem > 0:
                prefixes.add(elem)
                elem //= 10
        
        result = 0
        for elem in arr1:
            while elem > result:
                if elem in prefixes:
                    result = max(result, elem)
                    break
                else:
                    elem //= 10
        
        if result == 0:
            return 0
        return len(str(result))
            