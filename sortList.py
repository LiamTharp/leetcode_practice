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
        
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None

        l = self.sortList(head)
        r = self.sortList(second)

        return self.merge(l, r)

    def merge(self, l, r):

        print(f'Merging {l=} // {r=}', end= '')
        
        if l is None:
            return r
        elif r is None:
            return l
        
        start = ListNode(0)
        head = start

        while l and r:
            if l.val <= r.val:
                head.next = l
                l = l.next
            else:
                head.next = r
                r = r.next
            head = head.next
        
        head.next = l if r is None else r

        print(f' // {start.next}')
        return start.next
        




input = [5,1,2,4]

ll_input = LinkedList(input)

out = Solution.sortList(Solution(), ll_input.head)

print(out)

output = [1,2,3,4]
