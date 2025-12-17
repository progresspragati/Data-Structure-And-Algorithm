from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> int:
        i = 0
        first = head
        while i < n:
            first = first.next
            i += 1
        if first is None:
            return head.next
        second = head
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next

        return head





result = Solution()
node5 = ListNode(10, None)
node4 = ListNode(8, node5)
node3 = ListNode(6, node4)
node2 = ListNode(14, node3)
node1 = ListNode(2, node2)
head = result.removeNthFromEnd(node1, 2)
while head:
    print(head.val)
    head = head.next
