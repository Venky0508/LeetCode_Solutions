class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        ans = 1
        for i in range(len(s)):
            j = i + 2
            
            while j <= len(s):
                temp = list(s[i:j])
                check = set(temp)
                if len(temp) != len(check):
                    break
                j += 1
                if len(temp) > ans:
                    ans = len(temp)
        return ans

#         if s == "":
#             return 0

#         max_val = float("-inf")
#         temp_set = set()

    

#         for i in range(len(s)):
#             temp_set.add(s[i])
#             for j in range (i+1, len(s)):
#                 if s[j] not in temp_set:
#                     temp_set.add(s[j])
                
#                 else:
#                     n = len(temp_set)
#                     if max_val < n :
#                         max_val = n
#                     temp_set = set() 
#                     break
            
#             x = len(temp_set)
#             if x != 0 and max_val < x :
#                 max_val = x



        return int(max_val)