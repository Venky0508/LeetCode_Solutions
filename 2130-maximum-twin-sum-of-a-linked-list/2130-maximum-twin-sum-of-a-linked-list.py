# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = []
        start = head 
        while start != None:
            temp.append(start.val)
            start = start.next
        
        maxSum = float('-inf')
        n = len(temp)
        last = n - 1
        for i in range(n//2):
            first = temp[i]
            second = temp[last - i]
            total = first + second
            if total > maxSum:
                maxSum = total
        
        return maxSum





        