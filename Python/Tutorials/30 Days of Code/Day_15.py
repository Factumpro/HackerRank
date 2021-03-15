'''
Day 15: Linked List
(FIFO)

  Tutorial:
  https://realpython.com/linked-lists-python/

  linked lists have a performance advantage over normal lists when 
  implementing a queue (FIFO), in which elements are continuously inserted 
  and removed at the beginning of the list. But they perform similarly to 
  a list when implementing a stack (LIFO), in which elements are inserted 
  and removed at the end of the list.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method 
        if head is None:
            head = Node(data)
            self.tail = head
            #print(self.tail.data, self.tail.next, head.data, head.next,end=' - 0p\n')
        else: 
            node = Node(data)
            #print(self.tail.data, self.tail.next, head.data, head.next,end=' - 1p\n')
            self.tail.next = node
            #print(self.tail.data, self.tail.next, head.data, head.next,end=' - 2p\n')
            self.tail = node
            #print(self.tail.data, self.tail.next, head.data, head.next,end=' - 3p\n')
        
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  