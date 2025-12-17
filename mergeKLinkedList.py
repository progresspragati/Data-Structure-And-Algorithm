from typing import List, Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class Solution: 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for first in lists:
            while first:
                nodes.append(first.val)
                first = first.next
        nodes.sort()

        temp = ListNode(0)
        cur = temp
        for res in nodes:
            cur.next = ListNode(res)
            cur = cur.next
        return temp.next

    

result = Solution()
head = result.mergeKLists([[1,2,4],[1,3,5],[3,6]])
while head:
    print(head.val)