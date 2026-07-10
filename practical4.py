import time
from colorama import init, Fore, Style
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insert at position
    def insert_position(self, pos, data):

        if pos == 1:
            self.insert_begin(data)
            return

        temp = self.head
        count = 1

        while temp and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of bounds.")
            return

        new_node = Node(data)

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    # Delete beginning
    def delete_begin(self):

        if self.head is None:
            print("List is empty.")
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

        print("Node deleted from beginning.")

    # Delete end
    def delete_end(self):

        if self.head is None:
            print("List is empty.")
            return

        if self.head.next is None:
            self.head = None
            print("Node deleted.")
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None

        print("Node deleted at end.")

    # Delete position
    def delete_position(self, pos):

        if self.head is None:
            print("List is empty.")
            return

        if pos == 1:
            self.delete_begin()
            return

        temp = self.head
        count = 1

        while temp and count < pos:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of bounds.")
            return

        if temp.next:
            temp.next.prev = temp.prev

        temp.prev.next = temp.next

        print("Node deleted.")

    # Display
    def display(self):

        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        print("Doubly Linked List:")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # Search
    def search(self, key):

        temp = self.head
        pos = 1

        while temp:

            if temp.data == key:
                print("Element found at position", pos)
                return

            temp = temp.next
            pos += 1

        print("Element not found.")

    # Length
    def length(self):

        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        print("Length =", count)


dll = DoublyLinkedList()

while True:

    print("\n===== Doubly Linked List =====")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at position")
    print("4. Delete at beginning")
    print("5. Delete at end")
    print("6. Delete at specific position")
    print("7. Display")
    print("8. Search")
    print("9. Length")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value: "))
        dll.insert_begin(data)

    elif choice == 2:
        data = int(input("Enter value: "))
        dll.insert_end(data)

    elif choice == 3:
        pos = int(input("Enter position: "))
        data = int(input("Enter value: "))
        dll.insert_position(pos, data)

    elif choice == 4:
        dll.delete_begin()

    elif choice == 5:
        dll.delete_end()

    elif choice == 6:
        pos = int(input("Enter position: "))
        dll.delete_position(pos)

    elif choice == 7:
        dll.display()

    elif choice == 8:
        key = int(input("Enter element to search: "))
        dll.search(key)

    elif choice == 9:
        dll.length()

    elif choice == 10:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")
