class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        words = s.strip().split(' ')
        for i in range(0, len(words)):
            word = words[i].strip()
            if i != len(words) - 1 and word != "":
                ans = " " + word + ans
            else:
                ans = word + ans
        return ans 
            
        