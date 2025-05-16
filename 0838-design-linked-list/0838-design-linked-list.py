class Node:
    """A class representing a node in the linked list."""
    def __init__(self, val=0):
        self.val = val  # Value of the node
        self.next = None  # Pointer to the next node


class MyLinkedList:
    """A class implementing a singly linked list."""
    def __init__(self):
        self.head = None  # Pointer to the head of the linked list
        self.size = 0  # Size of the linked list to track the number of nodes

    def get(self, index):
        """Get the value of the index-th node in the linked list."""
        if index < 0 or index >= self.size:
            return -1  # Invalid index
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val):
        """Add a node of value val before the first element."""
        new_node = Node(val)  # Create a new node
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Update the head to the new node
        self.size += 1  # Increment the size of the linked list

    def addAtTail(self, val):
        """Append a node of value val as the last element."""
        new_node = Node(val)  # Create a new node
        if not self.head:  # If the linked list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Append the new node at the end
        self.size += 1  # Increment the size of the linked list

    def addAtIndex(self, index, val):
        """Add a node of value val before the index-th node."""
        if index < 0 or index > self.size:
            return  # Invalid index, do nothing
        if index == 0:
            self.addAtHead(val)  # Add at the head
        elif index == self.size:
            self.addAtTail(val)  # Add at the tail
        else:
            new_node = Node(val)
            current = self.head
            for _ in range(index - 1):  # Traverse to the node before the index
                current = current.next
            new_node.next = current.next  # Update pointers to insert the new node
            current.next = new_node
            self.size += 1  # Increment the size of the linked list

    def deleteAtIndex(self, index):
        """Delete the index-th node in the linked list."""
        if index < 0 or index >= self.size:
            return  # Invalid index, do nothing
        if index == 0:
            self.head = self.head.next  # Remove the head node
        else:
            current = self.head
            for _ in range(index - 1):  # Traverse to the node before the index
                current = current.next
            current.next = current.next.next  # Skip the node to delete
        self.size -= 1  # Decrement the size of the linked list
