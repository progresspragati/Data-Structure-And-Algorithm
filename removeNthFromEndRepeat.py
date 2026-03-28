from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        len_list = 0
        while cur:
            len_list += 1
            cur = cur.next
        i = 0
        if len_list == n:
            return head.next
        
        cur = head
        for _ in range(len_list - n- 1):
            cur = cur.next
        cur.next = cur.next.next
        return head
    
    def removeNthFromEndUsingRec(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(root:ListNode, n)->ListNode:
            if not root:
                return None
            root.next = rec(root.next, n)
            n[0] -= 1
            if n[0] == 0:
                return root.next
            return root
        return rec(head, [n])

result = Solution()
nodeA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(3)
nodeD = ListNode(4)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = None
head = result.removeNthFromEndUsingRec(nodeA, 2)
while head:
    print(head.val)
    head = head.next
            

        