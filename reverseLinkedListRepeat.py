# Definition for singly-linked list.
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
           nxt = cur.next
           cur.next = prev
           prev = cur
           cur = nxt

        return prev
            


result = Solution()
nodeA = ListNode(0)
nodeB = ListNode(1)
nodeC = ListNode(2)
nodeD = ListNode(3)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = None
head = result.reverseList(nodeA)
while head:
    print(head.val)
    head = head.next