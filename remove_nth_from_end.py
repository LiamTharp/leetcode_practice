# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head.next:
            return None

        fast = slow = head

        while fast.next:
            
            fast = fast.next
            
            if n < 0:
                slow = slow.next
            elif n <= 0:
                slow = slow.next

            n -= 1
        
        if slow == head:
            head = head.next
        else:
            slower.next = slow.next

        return head


vals = [1,2,2,1]

