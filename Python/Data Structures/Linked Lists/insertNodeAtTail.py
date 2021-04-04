def insertNodeAtTail(head, data):
    node = head
    if node is None:
        node = SinglyLinkedListNode(data)
        return node
    while node.next is not None:
        node = node.next
    node.next = SinglyLinkedListNode(data)
    return head
