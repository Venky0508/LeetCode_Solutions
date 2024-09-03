class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        for c in s:
            if c.isalpha() == True:
                c = c.lower()
                temp += c
            
            if c.isnumeric() == True:
                temp += c
        
        if temp == "":
            return True
        
        n = len(temp)
        if n % 2 == 0:
            i = int(n/2) - 1
            j = int(n/2)
        else:
            i = (n//2) - 1
            j = (n//2) + 1
            
        while i >= 0 and j < n:
            if temp[i] != temp[j]:
                return False
            i -= 1
            j += 1
        
        return True
            
        