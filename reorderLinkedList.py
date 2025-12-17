from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp_list = []
        # res_list = []
        while head:
            temp_list.append(head.val)
            head = head.next
        i = 0
        while i < len(temp_list)/2:
            if i == len(temp_list)-i-1:
                print(temp_list[i])
            else:
                print(temp_list[i])
                print(temp_list[len(temp_list)-i-1])
            i += 1

    def reorderList1(self, head: Optional[ListNode]) -> None:
        temp_list = []
        res_list = []
        while head:
            temp_list.append(head.val)
            head = head.next
        i = 0
        while i < len(temp_list)//2:
            if i == len(temp_list)-i-1:
                res_list.append(temp_list[i])
            else:
                res_list.append(temp_list[i])
                res_list.append(temp_list[len(temp_list)-i-1])
            i += 1
        return res_list
    
    def reorderList2(self, head: Optional[ListNode]) -> None:
        slow_node = head
        fast_node = head.next
        l1 = slow_node
        l2 = None
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        l2 = slow_node.next
        slow_node.next = None
        prev = None
        while l2:
            next = l2.next
            l2.next = prev
            prev = l2
            l2 = next 
        l2 = prev
        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2
    
result = Solution()
node5 = ListNode(10, None)
node4 = ListNode(8, node5)
node3 = ListNode(6, node4)
node2 = ListNode(14, node3)
node1 = ListNode(2, node2)

# res_val = result.reorderList2(node1)
# i = 0
# while i < len(res_val):
#     print(res_val[i])
#     i += 1
result.reorderList2(node1)
head = node1
while head:
    print(head.val)
    head = head.next