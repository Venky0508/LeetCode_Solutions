# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast = head
        slow = ListNode()
        
        slow.next = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        