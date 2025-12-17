from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp_slow = head
        slow_step = temp_slow
        temp = head.next.next
        fast_step = temp
        while slow_step and fast_step:
            if slow_step == fast_step:
                return True
            slow_step = temp_slow.next
            fast_step = temp.next.next 
        return False
    
result = Solution()
node5 = ListNode(9, None)
node4 = ListNode(2, node5)
node3 = ListNode(3, node4)
node2 = ListNode(11, node3)
node1 = ListNode(7, node2)

print(result.reverseList(node1))

