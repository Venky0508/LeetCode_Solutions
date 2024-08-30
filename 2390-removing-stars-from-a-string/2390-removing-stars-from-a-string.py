class Solution:
    def removeStars(self, s: str) -> str:
        final = ''

        for i in range(len(s)):
            if s[i] == '*':
                prev = len(final) - 1
                if prev != -1:
                    final = final[:-1]
        
            else:
                final += s[i]
  
        
        return final




        