#!/usr/bin/env python3

"""
    Queues and Stacks
    -----------------

    In Python Stack as LifoQueue and Queue as Queue

    Second solution (list type)
    ---------------------------
    class Solution:
        def __init__(self):
            self.lifo_ = []
            self.fifo_ = []

        def push_character(self, box):
            self.lifo_.append(box)

        def enqueue_character(self, box):
            self.fifo_.append(box)

        def pop_character(self):
            return self.lifo_.pop(-1)

        def dequeue_character(self):
            return self.fifo_.pop(0)
"""

from queue import Queue, LifoQueue


class Solution:
    def __init__(self):
        self.lifo_ = LifoQueue()
        self.fifo_ = Queue()

    def push_character(self, box):
        self.lifo_.put(box)

    def enqueue_character(self, box):
        self.fifo_.put(box)

    def pop_character(self):
        return self.lifo_.get()

    def dequeue_character(self):
        return self.fifo_.get()
