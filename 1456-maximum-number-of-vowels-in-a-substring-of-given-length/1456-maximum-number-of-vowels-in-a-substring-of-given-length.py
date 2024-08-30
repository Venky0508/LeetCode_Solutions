class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        length = len(s) - 1
        for i in s[:k]:
            if i in vowels:
                count += 1
            else:
                continue

        i = 0
        maxCount = count
        for j in range(k, len(s)):
            if s[j] in vowels:
                count += 1
            if s[i] in vowels:
                count -= 1
            i += 1
            if maxCount < count:
                maxCount = count
            if maxCount == k:
                break
        
        return maxCount
            
        
        return ans  
