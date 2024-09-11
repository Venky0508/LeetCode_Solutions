# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = []
        
        while head != None:
            temp.append(head.val)
            head = head.next
            
        if n > len(temp):
            return None
        
        if n != 1 and n!= 0:
            final = temp[:-n] + temp[-n+1:]
        elif n == len(temp):
            if n == 1:
                return None
            final = temp[-n+1:]
        else:
            final = temp[:-n]
        
        
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
        