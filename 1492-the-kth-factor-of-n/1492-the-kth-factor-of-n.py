class Solution:
    def kthFactor(self, n: int, k: int) -> int:        
        factors = [1, n]
        
        i = 2
        while i < n:
            if n % i == 0:
                factors.append(i)
            i += 1
            
        factors.sort()
        if k > len(factors):
            return -1
        
        return factors[k-1]
        