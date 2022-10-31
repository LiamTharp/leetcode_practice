from typing import Optional

class LinkedList:
    def __init__(self, arr = None):

        self.head = None

        if arr is not None:

            if len(arr) == 0:
                return None

            self.head = ListNode(arr[0])
            cur = self.head

        for x in arr[1:]:
            cur.next = ListNode(x)
            
            cur = cur.next

    def __repr__(self):

        print(self.head)

        


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        
        cur = self

        ll_str = []

        while cur:
            ll_str.append(cur.val)
            cur = cur.next

        return ", ".join(map(str,ll_str))
        


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        odd = head
        
        even = evenhead = head.next

        while even and even.next:
            
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

            
        odd.next = evenhead

        return head
        
        
input = [1,2,3]

ll_input = LinkedList(input)

sol = Solution()

test = sol.oddEvenList(ll_input.head)

print(test)

output = [1,3,5,2,4]
            
