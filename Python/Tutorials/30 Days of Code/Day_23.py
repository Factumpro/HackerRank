#!/usr/bin/env python3

"""
    BST Level-Order Traversal
    -------------------------

"""

import sys


class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                current = self.insert(root.left, data)
                root.left = current
            else:
                current = self.insert(root.right, data)
                root.right = current

        return root

    def level_order(self, root):
        if root is None:
            queue = []
        else:
            queue = [root]
        while queue:
            node = queue.pop()
            print(node.data, end=" ")
            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)

if __name__ == '__main__':
    bin_tree = Solution()
    root = None
    for _ in range(int(input())):
        data = int(input())
        root = bin_tree.insert(root, data)
    bin_tree.level_order(root)
