class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            total = 0
            while n > 0:
                x = n % 10
                total += x ** 2
                n //= 10
            
            if total == 1:
                return True
            n = total
        
        return False