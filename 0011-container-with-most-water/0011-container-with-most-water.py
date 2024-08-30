class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        start = 0
        end = len(height) - 1
        while start <= end:
            a = height[start]
            b = height[end]
            length = min(a, b)
            width = end - start
            area = length * width
            if area > maxArea:
                maxArea = area
            if a > b:
                end -= 1
            else:
                start += 1

        return maxArea



