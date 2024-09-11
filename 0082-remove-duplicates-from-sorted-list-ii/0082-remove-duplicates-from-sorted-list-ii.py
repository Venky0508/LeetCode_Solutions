# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = {}
        
        while head != None:
            if head.val not in temp:
                temp[head.val] = 1
                head = head.next
            else:
                temp[head.val] += 1
                head = head.next
                
        
        if len(temp.keys()) == 0:
            return None
        
        final = []
        for k, v in temp.items():
            if v == 1:
                final.append(k)
        if len(final) == 0:
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
                
        
        
        