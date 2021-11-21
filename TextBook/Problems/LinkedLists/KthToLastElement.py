def KthToLastElement(head, k):
    # need slow and fast pointers
    dummy_head = ListNode(0)
    dummy_head.next = head
    
    slow = fast = head
    for _ in range(k+1):
        fast = fast.next
    
    while fast:
        fast = fast.next
        slow = slow.next
    
    return slow.next.val
# The time complexity is O(n) and the space complexity is O(n).
