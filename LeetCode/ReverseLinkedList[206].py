# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:  # while head is not None
            next_node = head.next  # save the next node
            head.next = prev  # reverse the link
            prev = head  # move prev to the next node
            head = next_node  # move head to the next node
        return prev  # return the new head
# Time complexity is O(n).
