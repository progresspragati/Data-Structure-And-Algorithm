from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()

        res = ListNode(0)
        cur = res
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return res.next
    
result = Solution()
node1_3 = ListNode(4, None)
node1_2 = ListNode(2, node1_3)
node1_1 = ListNode(1, node1_2)

node2_3 = ListNode(5, None)
node2_2 = ListNode(3, node2_3)
node2_1 = ListNode(1, node2_2)

node3_2 = ListNode(8, None)
node3_1 = ListNode(7, node3_2)

result.mergeKLists([node1_1, node2_1, node3_1])
head = result.mergeKLists([node1_1, node2_1, node3_1])

while head:
    print(head.val)
    head = head.next