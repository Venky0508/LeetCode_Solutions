# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        
        start = head
        temp = []
        while start != None:
            temp.append(start.val)
            start = start.next
        
        ans = ListNode(temp[-1])
        for i in range(len(temp)-2, -1, -1):
            new = ListNode(temp[i])
            if i == len(temp) - 2:
                ans.next = new
                prev = new
            else:
                prev.next = new
                prev = new 

        return ans


        