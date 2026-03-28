from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length_list = 0
        cur = head
        temp = head
        while cur:
            length_list += 1
            cur = cur.next
        i = 0
        while i < length_list//2:
            temp = temp.next
            i += 1
        mid = temp.next
        temp.next = None

        def reverseList(node:Optional[ListNode]):
            cur = node
            prev = None
            global length_list
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        reverse_head = reverseList(mid)
        first = head
        second = reverse_head
        while second:
           temp1 = first.next
           temp2 = second.next
           first.next = second
           second.next = temp1
           first = temp1
           second = temp2

    def reorderListUsingSlowFastPointer(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
    
    def reorderListUsingRec(self, head: Optional[ListNode]) -> None:
        def rec(root:ListNode, cur:ListNode)-> ListNode:
            if not cur:
                return root
            root = rec(root, cur.next)
            if not root:
                return None
            temp = None
            if root == cur or root.next == cur:
                cur.next = None
            else:
                temp = root.next
                root.next = cur
                cur.next = temp
            return temp
        head = rec(head, head.next)
        
result = Solution()
nodeA = ListNode(1)
nodeB = ListNode(2)
nodeC = ListNode(3)
nodeD = ListNode(4)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = None
result.reorderListUsingRec(nodeA)
# result.reorderList(nodeA)
head = nodeA
while head:
    print(head.val)
    head = head.next
