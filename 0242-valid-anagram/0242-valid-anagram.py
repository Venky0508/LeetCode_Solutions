class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letterMap = {}
        
        for i in s:
            if i not in letterMap:
                letterMap[i] = 1
            else:
                letterMap[i] += 1
        
        for j in t:
            if j not in letterMap:
                return False
            else:
                count = letterMap[j]
                if count == 0:
                    return False
                else:
                    letterMap[j] -= 1
        
        return True