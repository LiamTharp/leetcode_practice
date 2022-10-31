# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(head: Optional[ListNode]) -> bool:
        
        if head.next is None:
            return True

        val1 = head.next
        val2 = head.next.val
        
        while head.next is not None:
            
            

            head = head.next

            


        
        return True  
