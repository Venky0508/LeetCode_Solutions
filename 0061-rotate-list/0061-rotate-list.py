# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        temp = []
        
        while head != None:
            temp.append(head.val)
            head = head.next
            
        k = k % len(temp)
        final = temp[-k:] + temp[:-k]
        
        front = ListNode(final[0])
        i = 1
        flag = True
        
        while i < len(final):
            node = ListNode(final[i])
            
            if flag == True:
                front.next = node
                pointer = node
                flag = False
            else:
                pointer.next = node
                pointer = node
                
            i += 1
            
        return front
            
            