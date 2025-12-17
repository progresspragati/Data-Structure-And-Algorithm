from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_result = ListNode(0, None)
        head = list_result
        while list1 and list2:
            if list1.val < list2.val:
                list_result.next = list1
                list1 = list1.next
                list_result = list_result.next
            else:
                list_result.next = list2
                list2 = list2.next
                list_result = list_result.next
        list_result.next = list1 if list1 else list2
        return head.next


result = Solution()
node1_3 = ListNode(4, None)
node1_2 = ListNode(2, node1_3)
node1_1 = ListNode(1, node1_2)

node2_3 = ListNode(4, None)
node2_2 = ListNode(3, node2_3)
node2_1 = ListNode(1, node2_2)

head = result.mergeTwoLists(node1_1, node2_1)
while head:
    print(head.val)
    head = head.next