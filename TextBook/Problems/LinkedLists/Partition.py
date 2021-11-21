def Partition(head, partition):
    less = Node(None)
    greaterEqual = Node(None)

    # set up pointers to traverse the linked lists
    headL = less
    headG = greaterEqual

    # create iterator variable
    cur = head

    while cur:
        if cur.val >= partition:
            headG.next = cur  # set next value in Linked List to cur
            headG = headG.next  # move forward to set up next addition
        else:
            headL.next = cur  # set next value in Linked List to cur
            headL = headL.next  # move forward to set up next addition
        cur = cur.next  # move to next node in Linked List

    headL.next = headG.next  # combine both Linked Lists

    return less
# The time complexity is O(n) and the space complexity is O(1)
