#!/usr/bin/env python3

"""
    Linked List (FIFO)
    ------------------

    Linked lists have a performance advantage over normal lists when
    implementing a queue (FIFO), in which elements are continuously inserted
    and removed at the beginning of the list. But they perform similarly to
    a list when implementing a stack (LIFO), in which elements are inserted
    and removed at the end of the list.

    https://realpython.com/linked-lists-python/
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        if head is None:
            head = Node(data)
            self.tail = head
    # print(self.tail.data, self.tail.next, head.data, head.next,end=' - 0p\n')
        else:
            node = Node(data)
    # print(self.tail.data, self.tail.next, head.data, head.next,end=' - 1p\n')
            self.tail.next = node
    # print(self.tail.data, self.tail.next, head.data, head.next,end=' - 2p\n')
            self.tail = node
    # print(self.tail.data, self.tail.next, head.data, head.next,end=' - 3p\n')
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

if __name__ == '__main__':
    my_list = Solution()
    head = None
    for _ in range(int(input())):
        data = int(input())
        head = my_list.insert(head, data)
    my_list.display(head)
