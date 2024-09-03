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