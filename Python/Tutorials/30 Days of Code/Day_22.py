'''
30/Day 22: Binary Search Trees

  https://www.hackerrank.com/challenges/30-binary-search-trees/problem
'''

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root!=None: 
            len_w_root = self._getHeight(root, 0)
            len_wo_root = len_w_root -1
            return len_wo_root
        else:
            return 0

    def _getHeight(self, root, cure_height):
        if root == None: 
            return cure_height
        left_height = self._getHeight(root.left, cure_height+1)
        right_heigt = self._getHeight(root.right, cure_height+1)
        return max(left_height, right_heigt)
        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       