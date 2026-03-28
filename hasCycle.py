from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def hasCycleUsingHashSet(self, head: Optional[ListNode])-> bool:
        visited_node = set()
        while head:
            if head in visited_node:
                return True
            visited_node.add(head)
            head = head.next
        return False

    
result = Solution()
nodeA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(3)
nodeD = ListNode(4)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeB
print(result.hasCycle(nodeA))
print(result.hasCycleUsingHashSet(nodeA))