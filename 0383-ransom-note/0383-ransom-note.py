class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for i in range(len(magazine)):
            key = magazine[i]
            if key not in letters:
                letters[key] = 1
            else:
                letters[key] += 1
        
        for j in ransomNote:
            if j not in letters:
                return False
            else:
                count = letters[j]
                if count == 0:
                    return False
                else:
                    letters[j] -= 1
        return True
        