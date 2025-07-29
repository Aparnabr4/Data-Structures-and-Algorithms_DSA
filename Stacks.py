"""
A stack is a linear data structure that follows the LIFO (Last-In-First-Out) principle. The last element added to the stack is the first one to be removed.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class Stack:
    def __init__(self):
        self._top = None
        self._size = 0
        self._max_allowed_size = 10

    def push(self, value):
        if self._max_allowed_size == self._size:
            raise Exception("Stack is Full")

        new_node = Node(value)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
        return self

    def pop(self):
        if self._size == 0:
            self._top.next = None
        else:
            popped_node = self._top
            self._top = popped_node.next
            popped_node.next = None
            self._size -= 1
        return popped_node.value

    def peek(self):
        return self._top.value if self._top else None

    def clear(self):
        self._top = None
        self._size = 0
        return self

my_stack = Stack()

my_stack.push("Google")
my_stack.push("Twitter")
my_stack.push("Instagram")

print(my_stack.peek())


"""
 📌 Use Cases of Stack:
  
Undo functionality in text editors
Backtracking (e.g., maze solving, recursion stack)
Browser history (back button)
Expression evaluation (postfix, infix)
Function call stack in programming languages
"""

