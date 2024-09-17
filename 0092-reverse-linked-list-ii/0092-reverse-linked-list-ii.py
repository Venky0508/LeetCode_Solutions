# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        temp = []
        while head != None:
            temp.append(head.val)
            head = head.next
        
        x = temp[left-1:right]   
        final = temp[:left-1] + x[::-1] + temp[right:]
        front = ListNode(final[0])
        flag = True
        for i in final[1:]:
            node = ListNode(i)
            if flag == True:
                front.next = node
                prev = node
                flag = False
            else:
                prev.next = node
                prev = node
                
        return front
            
        