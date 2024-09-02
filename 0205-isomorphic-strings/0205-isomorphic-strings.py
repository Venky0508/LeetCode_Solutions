class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letterMap = {}
        for i in range(len(s)):
            key = s[i]
            value = t[i]
                
            if key not in letterMap:
                if value not in letterMap.values():
                    letterMap[key] = value
                else:
                    return False
                
            else:
                val = letterMap[key]
                if val != value:
                    return False
        return True
                