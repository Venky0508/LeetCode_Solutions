# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = []
        greater = []
        
        while head != None:
            value = head.val
            if value < x:
                less.append(value)
            else:
                greater.append(value)
                
            head = head.next
            
#         if less != []:
#             less.sort()
        
#         if greater != []:
#             greater.sort()
        
        final = less + greater
        if final == []:
            return None
        
        front = ListNode(final[0])
        for i in range(1, len(final)):
            node = ListNode(final[i])
            if i == 1:
                front.next = node
                prev = node
            else:
                prev.next = node
                prev = node
                
        return front
        