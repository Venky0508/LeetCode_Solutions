class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.strip().split(" ")
        
        if len(s) != len(pattern):
            return False
        
        wordMap = {}
        for i in range(len(s)):
            key = pattern[i]
            value = s[i]
            if key not in wordMap:
                if value not in wordMap.values():
                    wordMap[key] = value
                else:
                    return False
            else:
                val = wordMap[key]
                if val != value:
                    return False
        return True
                