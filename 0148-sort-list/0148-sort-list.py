# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        
        while head != None:
            temp.append(head.val)
            head = head.next
        
        if temp == []:
            return None
        
        temp.sort()
        ans = ListNode(temp[0])
        if len(temp) == 1:
            return ans
        
        flag = True
        for i in temp[1:]:
            new = ListNode(i)
            if flag == True:
                ans.next = new
                flag = False
                prev = new
            else:
                prev.next = new
                prev = new
        
        return ans
            
        