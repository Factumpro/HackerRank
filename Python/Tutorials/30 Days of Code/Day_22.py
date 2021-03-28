#!/usr/bin/env python3

"""
    Binary Search Trees
    -------------------

"""


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

    def get_height(self, root):
        if root is not None:
            height_w_root = self.get_height_(root, 0)
            height_wo_root = height_w_root-1
            return height_wo_root
        else:
            return 0

    def get_height_(self, root, cure_height):
        if root is None:
            return cure_height
        left_height = self.get_height_(root.left, cure_height+1)
        right_height = self.get_height_(root.right, cure_height+1)

        return max(left_height, right_height)

if __name__ == '__main__':
    bin_tree = Solution()
    root = None
    for _ in range(int(input())):
        data = int(input())
        root = bin_tree.insert(root, data)
    tree_height = bin_tree.get_height(root)
    print(tree_height)
