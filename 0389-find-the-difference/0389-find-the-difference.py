class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        
        s = sorted(s)
        t = sorted(t)

        for i in range(len(t)):
            if i == len(s):
                return t[i]
            if s[i] != t[i] and i != len(s):
                return t[i]
            
            