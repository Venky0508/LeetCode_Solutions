class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency_map = {}

        for i in s:
            if i not in frequency_map:
                frequency_map[i] = 1
            else:
                frequency_map[i] += 1

        for k, v in frequency_map.items():
            if v == 1:
                return s.index(k)

        return -1