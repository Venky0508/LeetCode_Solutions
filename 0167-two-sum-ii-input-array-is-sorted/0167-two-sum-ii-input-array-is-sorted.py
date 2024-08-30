class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j =len(numbers) - 1
        
        while i < j:
            first = numbers[i]
            second = numbers[j]
            total= first+second
            if total == target:
                return [i+1, j+1]
            elif total > target:
                j -= 1
            else:
                i += 1
        
        return []
            