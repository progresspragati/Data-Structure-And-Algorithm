from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        dummy = ListNode()
        cur = dummy
        while True:
            min_node = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if min_node == -1 or lists[min_node].val > lists[i].val:
                    min_node = i
            if min_node == -1:
                break
            cur.next = lists[min_node]
            lists[min_node] = lists[min_node].next
            cur = cur.next
        return dummy.next
    
    def mergeKListsUsingHeap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        dummy = ListNode()
        cur = dummy
        while heap:
            val, i, node = heapq.heappop(heap)

            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
    
result = Solution()
nodeA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(4)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = None

nodeA1 = ListNode(1)
nodeB1 = ListNode(3)
nodeC1 = ListNode(5)
nodeA1.next = nodeB1
nodeB1.next = nodeC1
nodeC1.next = None

nodeA2 = ListNode(3)
nodeB2 = ListNode(6)
nodeA2.next = nodeB2
nodeB2.next = None

result = Solution()
head = result.mergeKListsUsingHeap([nodeA, nodeA1, nodeA2])

while head:
    print(head.val)
    head = head.next