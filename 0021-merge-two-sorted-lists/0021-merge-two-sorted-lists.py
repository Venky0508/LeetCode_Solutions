# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        elif list1 is None and list2 is None:
            return None
        
        temp = []
        
        while list1 is not None:
            temp.append(list1.val)
            list1 = list1.next
            
        while list2 is not None:
            temp.append(list2.val)
            list2 = list2.next
        
        temp.sort()
        head = ListNode(temp[0])
        prev = head
        i = 1
        while i < len(temp):
            new = ListNode(temp[i])
            prev.next = new
            prev = new
            i += 1
                
        return head