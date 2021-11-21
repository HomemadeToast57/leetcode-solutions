# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # dummy node
        tail = dummy  # tail node

        while l1 and l2:  # while both lists are not empty
            if l1.val < l2.val:  # if l1 is smaller
                tail.next = l1  # add l1 to tail
                l1 = l1. next  # move l1 to next node
            else:  # if l2 is smaller
                tail.next = l2  # add l2 to tail
                l2 = l2.next  # move l2 to next node
            tail = tail.next  # move tail to next node

        if l1:  # if l1 is not empty
            tail.next = l1  # add l1 to tail
        elif l2:  # if l2 is not empty
            tail.next = l2  # add l2 to tail

        return dummy.next  # return dummy node
# Time complexity of O(n+m) and space complexity of O(1)
