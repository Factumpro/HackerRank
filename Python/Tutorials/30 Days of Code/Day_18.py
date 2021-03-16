''''
Day 18: Queues and Stacks

''''

''''
As list type

class Solution:
    def __init__(self):
        self._stack1 = []
        self._queue1 = []
    def pushCharacter(self, box):      
        self._stack1.append(box)
    def enqueueCharacter(self, box):
        self._queue1.append(box)
    def popCharacter(self):
        return self._stack1.pop(-1)   
    def dequeueCharacter(self):
        return self._queue1.pop(0)
''''

''''
With the library queue 
(In Python Stack as LifoQueue and Queue as Queue)
''''
from queue import Queue, LifoQueue

class Solution:
# get()
# put()
# empty()
    def __init__(self):        
        self._stack1 = LifoQueue()
        self._queue1 = Queue()
    # Write your code here
    def pushCharacter(self, box):
        self._stack1.put(box)
    def enqueueCharacter(self, box):
        self._queue1.put(box)
    def popCharacter(self):
        return self._stack1.get()
    def dequeueCharacter(self):
        return self._queue1.get()