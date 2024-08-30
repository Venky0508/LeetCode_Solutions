class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(' ')
        last = words[-1]
        ans = len(last)
        return ans
        
        