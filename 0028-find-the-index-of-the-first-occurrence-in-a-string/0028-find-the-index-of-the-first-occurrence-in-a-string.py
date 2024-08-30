class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        n = len(needle)
        for i in range(len(haystack)):
            if i+n > len(haystack):
                break
            word = haystack[i:i+n]
            if word == needle:
                return i
        
        return -1
        