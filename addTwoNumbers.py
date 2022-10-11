# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node_ptr = ListNode()
        head_node = node_ptr
        carryover = 0
        while l1 != None or l2 != None or carryover != 0:
            val1 = l1.val if l1!=None else 0
            val2 = l2.val if l2!=None else 0
            new_val, carryover = (val1 + val2 + carryover)%10, (val1 + val2 + carryover)//10
            new_node = ListNode(new_val)
            node_ptr.next = new_node
            node_ptr = new_node
            l1,l2 = l1.next if l1 != None else None,l2.next if l2 != None else None
        return head_node.next
