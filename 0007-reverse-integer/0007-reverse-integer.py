class Solution:
    def reverse(self, x: int) -> int:
        digits = []
        if x == 0:
            return 0
        
        
        
        if x < 0:
            flag = True
            x = x * -1
        else:
            flag = False
        
        
        while x > 0:
            temp = x % 10
            digits.append(temp)
            x = x//10
            
        result = ''
        for i in digits:
            result += str(i)
        
        if flag == True:
            if (-1) * int(result) <= ((-2) ** 31)  or (-1) * int(result) >= (2 ** 31) - 1 :
                return 0
            else:
                return (-1) * int(result)
        
        if int(result) <= ((-2) ** 31)  or int(result) >= (2 ** 31) - 1 :
            return 0
            
        return int(result)
            
            