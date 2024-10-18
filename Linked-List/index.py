class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head  # Next for new node becomes the   current head
        self.head = new_node  # Head now points to the new node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        # If the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return
        last = self.head

        # Otherwise, traverse the list to find the last node
        while last.next:
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next
        print()  # Ensures the output is followed by a new line
