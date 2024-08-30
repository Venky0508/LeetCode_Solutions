class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ''
        count = 1
        prev = chars[0]
        s += prev 

        for j in range(1, len(chars)):
            new = chars[j]
            if new == prev:
                count += 1
                prev = new

            else:
                if count > 1:
                    s += str(count)
                s += new
                count = 1
                prev = new
        
        if count != 1:
            s += str(count)
            

        for a in range(len(s)):
            if chars[a] != s[a]:
                chars[a] = s[a]

        return len(s)




