from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
           temp = cur.next
           cur.next = prev
           prev = cur
           cur = temp
        return prev
        
result = Solution()
node5 = ListNode(9, None)
node4 = ListNode(2, node5)
node3 = ListNode(3, node4)
node2 = ListNode(11, node3)
node1 = ListNode(7, node2)

head = result.reverseList(node1)
while head:
    print(head.val)
    head = head.next
        