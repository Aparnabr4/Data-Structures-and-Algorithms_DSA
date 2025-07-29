class Node:
    def __init__(self, value):
        self.value = value      # Store the node's value
        self.next = None        # Pointer to the next node (default is None)


class SinglyLinkedList:
    def __init__(self):
        self.head = None        # First node in the list
        self.tail = None        # Last node in the list
        self._length = 0        # Keep track of the number of nodes

    def append(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if not self._length:    # If the list is empty
            self.head = self.tail = new_node  # Head and tail both point to the new node
        else:
            self.tail.next = new_node   # Link current tail to the new node
            self.tail = new_node        # Move the tail to the new node
        self._length += 1       # Increment the size of the list
        return self

    def prepend(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if not self._length:    # If the list is empty
            self.head = self.tail = new_node  # Head and tail both point to the new node
        else:
            new_node.next = self.head  # New node points to the current head
            self.head = new_node       # Move head to the new node
        self._length += 1       # Increment the size of the list
        return self

    def pop_left(self):
        if self._length == 0:   # If the list is empty
            return None
        former_head = self.head         # Store the current head
        self.head = self.head.next      # Move head to the next node
        self._length -= 1               # Decrement size
        if self._length == 0:           # If list is now empty
            self.tail = None            # Also reset the tail
        return former_head.value        # Return the removed value

    def pop_right(self):
        if self._length == 0:   # If the list is empty
            return None
        former_tail = self.tail         # Store the current tail

        if self._length == 1:           # If only one node exists
            self.head = self.tail = None
        else:
            current = self.head
            # Traverse to the second-last node
            while current.next != self.tail:
                current = current.next
            current.next = None        # Remove last node
            self.tail = current        # Update tail to second-last node

        self._length -= 1              # Decrement size
        return former_tail.value       # Return the removed value

    def reverse(self):
        prev = None                    # Will store the previous node (starts as None)
        current = self.head            # Start from head
        self.tail = self.head          # Tail will become the old head

        while current:
            next_node = current.next   # Store the next node
            current.next = prev       # Reverse the pointer
            prev = current            # Move prev forward
            current = next_node       # Move current forward

        self.head = prev              # Update head to the new front node
        return self

    def print_list(self):
        current = self.head           # Start from head
        while current:
            print(current.value, end=" -> ")  # Print each value
            current = current.next           # Move to next node
        print("None")                         # End of list

    def size(self):
        return self._length           # Return the number of elements



my_list = SinglyLinkedList()         # Create a new linked list

my_list.append(10)                   # Add 10 at the end
my_list.append(20)                   # Add 20 at the end
my_list.prepend(30)                  # Add 30 at the beginning

print("Original List:")
my_list.print_list()                 # 30 -> 10 -> 20 -> None

print("Head:", my_list.head.value)   # 30
print("Tail:", my_list.tail.value)   # 20

print("\nAfter popping right:", my_list.pop_right())  # Removes 20
my_list.print_list()                 # 30 -> 10 -> None

print("\nAfter popping left:", my_list.pop_left())    # Removes 30
my_list.print_list()                 # 10 -> None

print("\nAfter reversing:")
my_list.reverse()                    # Reverse the list
my_list.print_list()                 # 10 -> None

print("Size of list:", my_list.size())  # 1
