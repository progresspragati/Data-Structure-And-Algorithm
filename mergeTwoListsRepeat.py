from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            tail.next = list1 if list1 else list2
        return dummy.next

result = Solution()
nodeA = ListNode(0)
nodeB = ListNode(1)
nodeC = ListNode(2)
nodeD = ListNode(4)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = None

nodeA1 = ListNode(0)
nodeB1 = ListNode(1)
nodeC1 = ListNode(3)
nodeD1 = ListNode(5)
nodeA1.next = nodeB1
nodeB1.next = nodeC1
nodeC1.next = nodeD1
nodeD1.next = None
head = result.mergeTwoLists(nodeA, nodeA1)
while head:
    print(head.val)
    head = head.next
