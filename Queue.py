"""
A queue is a linear data structure that follows the FIFO (First-In-First-Out) principle. The first element added is the first to be removed.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def enqueue(self, value):
        new_element = Node(value)
        if not self._length:
            self.head = self.tail = new_element
        else:
            self.tail.next = new_element
            self.tail = new_element
        self._length += 1
        return self

    def dequeue(self, value):
        if not self._length:
            raise Exception("Empty Queue")

        popped_element = self.head
        self.head = popped_element.next
        popped_element.next = None
        self._length -= 1
        return self


    def peek(self):
        return self.tail.value if self.tail else None

    def clear(self):
        self.tail = None
        self.head = None
        self._lenght = 0
        return self


my_stack = Queue()

my_stack.enqueue(12)
my_stack.enqueue(14)
my_stack.enqueue(16)
my_stack.enqueue(18)

print(my_stack.peek())
print(my_stack.clear())
print(my_stack.peek())


# --------------------------------------------------- In-Build ---------------------------------------------------
from collections import deque

queue = deque()

queue.append("Twitter")     # Enqueue
queue.append("Meta")
queue.append("Facebook")
queue.append("Amazon")

print("Front element:", queue[0])  # 10
print(queue.popleft())  # Dequeue 10
print(queue.popleft())  # Dequeue 20


"""
📌 Use Cases of Queue:
 
CPU/Task scheduling
Printer queue
Breadth-First Search (BFS)
Message queues (Kafka, RabbitMQ)
Call center systems (first-come-first-served) 
 """