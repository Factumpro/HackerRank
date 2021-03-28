#!/usr/bin/env python3

"""
    More Linked Lists
    -----------------

    Time Complexity: O(n)

    def removeDuplicates(self,head):
    # Example with dictionary and not sorted (from discussions)
        if head == None:
            return head
        fptr = head.next
        sptr = head
        ha = {}
        while fptr:
            if sptr.data not in ha:
                ha[sptr.data] = True
            if fptr.data in ha:
                sptr.next = fptr.next
                fptr = fptr.next
                continue
            sptr = fptr
            fptr = fptr.next

        return head
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        noname = Node(data)
        if head is None:
            head = noname
        elif head.next is None:
            head.next = noname
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = noname

        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def remove_duplicates(self, head):
        if head is None:
            return head
        current = head
        head = None
        new_list = []
        while current:
            new_list.append(current.data)
            current = current.next
        new_list = set(new_list)
        new_list = list(new_list)
        for i in new_list:
            data = i
            head = self.insert(head, data)

        return head

if __name__ == '__main__':
    linked_list = Solution()
    root = None
    for _ in range(int(input())):
        data = int(input())
        head = linked_list.insert(head, data)
    head = linked_list.remove_duplicates(head)
    linked_list.display(head)
