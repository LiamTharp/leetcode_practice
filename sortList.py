from typing import Optional
# Definition for singly-linked list.
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        elif not head.next:
            return head

        front = head
        swap = 0

        while True:
            
            if head.next.val < head.val:
                val = head.next.val
                head.next.val = head.val
                head.val = val
                swap += 1

            if head.next.next:
                head = head.next
            elif swap == 0:
                break
            else:
                head = front
                swap = 0
                continue
            
            
        return front



input = [2,1]

ll_input = LinkedList(input)

sol = Solution()
out = sol.sortList(ll_input.head)

print(out)

output = [1,2,3,4]
