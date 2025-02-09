class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'

        if num < 0:
            sign = -1
        else:
            sign = 1

        n = abs(num)
        ans = ""
        while n > 0:
            ans += str(n % 7)
            n = int(n/7)
        
        ans = ans[::-1]

        if sign == -1:
            return '-' + ans
        else:
            return ans
