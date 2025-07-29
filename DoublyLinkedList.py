class DNode:
    def __init__(self, value):
        self.value = value      # Store the node's value
        self.prev = None        # Pointer to the previous node
        self.next = None        # Pointer to the next node


class DoublyLinkedList:
    def __init__(self):
        self.head = None        # Start of the list
        self.tail = None        # End of the list
        self._length = 0        # Length of the list

    def append(self, value):
        new_node = DNode(value)
        if not self.head:       # If list is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # Link old tail to new node
            new_node.prev = self.tail  # Link new node back to old tail
            self.tail = new_node       # Move tail to new node
        self._length += 1
        return self

    def prepend(self, value):
        new_node = DNode(value)
        if not self.head:       # If list is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head  # Link new node to old head
            self.head.prev = new_node  # Link old head back to new node
            self.head = new_node       # Move head to new node
        self._length += 1
        return self

    def pop_left(self):
        if not self.head:
            return None
        removed_node = self.head
        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.head = self.head.next    # Move head to next node
            self.head.prev = None         # Remove backward link
        self._length -= 1
        return removed_node.value

    def pop_right(self):
        if not self.tail:
            return None
        removed_node = self.tail
        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev    # Move tail backward
            self.tail.next = None         # Remove forward link
        self._length -= 1
        return removed_node.value

    def reverse(self):
        current = self.head
        self.tail = self.head     # After reverse, old head becomes new tail

        while current:
            # Swap next and prev pointers
            current.prev, current.next = current.next, current.prev
            current = current.prev  # Move to the previous node (which is now next)

        # After loop, set new head
        if self.tail:
            self.head = self.tail.prev

        return self

    def print_forward(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def print_backward(self):
        current = self.tail
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")

    def size(self):
        return self._length


dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.prepend(5)

print("Forward:")
dll.print_forward()      # 5 <-> 10 <-> 20 <-> None

print("Backward:")
dll.print_backward()     # 20 <-> 10 <-> 5 <-> None

print("Pop left:", dll.pop_left())   # Removes 5
print("Pop right:", dll.pop_right()) # Removes 20

print("After pops:")
dll.print_forward()      # 10 <-> None

print("After reverse:")
dll.reverse()
dll.print_forward()      # 10 <-> None

print("Size:", dll.size())  # 1
