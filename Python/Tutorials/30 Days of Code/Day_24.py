'''
Day 24: More Linked Lists

  https://www.hackerrank.com/challenges/30-linked-list-deletion/problem
'''

'''
with dictionary and not sorted (Discussions)

def removeDuplicates(self,head):
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
'''


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        if head == None:
            return head
        current = head
        head = None

        _lst = list()
        while current:
            _lst.append(current.data)
            current = current.next
        _lst=set(_lst)
        _lst=list(_lst)
        for i in _lst:
            data=i
            head=self.insert(head,data)  
        return head

T=int(input())
mylist= Solution()
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 