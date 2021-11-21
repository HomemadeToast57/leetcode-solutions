def DeleteMiddleNode(node):
    node.val = node.next.val
    node.next = node.next.next
# The time complexity is O(1) and the space complexity is O(1).
