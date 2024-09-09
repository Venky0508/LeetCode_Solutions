# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        
        while l1 != None:
            value = l1.val
            num1 += str(value)
            l1 = l1.next
            
        while l2 != None:
            value = l2.val
            num2 += str(value)
            l2 = l2.next
            
        x = int(num1[::-1])
        y = int(num2[::-1])
        
        z = x + y
        num3 = str(z)
        prev = ListNode(int(num3[-1]))
        
        i = len(num3) - 2
        flag = True
        
        while i >= 0:
            temp = int(num3[i])
            node = ListNode(temp)
            if flag == True:
                prev.next = node
                pointer = node
                flag = False
            else:
                pointer.next = node
                pointer = node
                
            i -= 1
            
        return prev
        
        