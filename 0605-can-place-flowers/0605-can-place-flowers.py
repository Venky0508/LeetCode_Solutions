class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 1 and n > 0:
            return False
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n > 1:
            return False
        if len(flowerbed) == 2 and 1 in flowerbed and n > 0:
            return False
        if len(flowerbed) == 2 and 1 not in flowerbed and n <= 1:
            return True
        if len(flowerbed) == 2 and 1 not in flowerbed and n > 1:
            return False
        
        ans = 0
        
        if flowerbed[1] == 0 and flowerbed[0] == 0:
            ans += 1
            flowerbed[0] = 1
        
        prev = flowerbed[0]
        
        for i in range(1, len(flowerbed)):
            new = flowerbed[i]
            if i+1 < len(flowerbed):
                nextVal = flowerbed[i+1]
                if prev == 0 and nextVal == 0 and new == 0:
                    ans += 1
                    flowerbed[i] = 1
                    prev = flowerbed[i]
                else:
                    prev = new
            else:
                if prev == 0 and new == 0:
                    ans += 1
                    flowerbed[i] = 1
                    prev = flowerbed[i]
    
        
        if n <= ans:
            return True
        else:
            return False
                
                