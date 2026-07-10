import time
from colorama import init, Fore, Style

init(autoreset=True)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(Fore.GREEN + "Node inserted at beginning.")

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print(Fore.GREEN + "Node inserted at end.")

    def insert_position(self, data, pos):
        if pos == 0:
            self.insert_beginning(data)
            return

        temp = self.head
        count = 0

        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print(Fore.RED + "Invalid position.")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

        print(Fore.GREEN + "Node inserted successfully.")


    def delete_value(self, value):
        temp = self.head

        if temp is None:
            print(Fore.RED + "List is empty.")
            return

        if temp.data == value:
            self.head = temp.next
            print(Fore.GREEN + "Node deleted.")
            return

        prev = None

        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp is None:
            print(Fore.RED + "Value not found.")
            return

        prev.next = temp.next
        print(Fore.GREEN + "Node deleted.")

    def delete_index(self, index):
        if self.head is None:
            print(Fore.RED + "List is empty.")
            return

        temp = self.head

        if index == 0:
            self.head = temp.next
            print(Fore.GREEN + "Node deleted.")
            return

        prev = None
        count = 0

        while temp and count < index:
            prev = temp
            temp = temp.next
            count += 1

        if temp is None:
            print(Fore.RED + "Invalid index.")
            return

        prev.next = temp.next
        print(Fore.GREEN + "Node deleted.")


    def display(self):
        if self.head is None:
            print(Fore.YELLOW + "List is empty.")
            return

        temp = self.head

        print(Fore.CYAN + "Linked List:")

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


sll = SinglyLinkedList()

while True:
    print(Fore.BLUE + Style.BRIGHT + "\nSingly Linked List Operations")
    print(Fore.BLUE + "1. Insert at beginning")
    print(Fore.BLUE + "2. Insert at end")
    print(Fore.BLUE + "3. Insert at position")
    print(Fore.BLUE + "4. Delete by value")
    print(Fore.BLUE + "5. Delete by index")
    print(Fore.BLUE + "6. Display the list")
    print(Fore.BLUE + "7. Exit")

    choice = input(Fore.YELLOW + "Enter your choice: ")

    if choice == "1":
        data = int(input("Enter value: "))
        sll.insert_beginning(data)

    elif choice == "2":
        data = int(input("Enter value: "))
        sll.insert_end(data)

    elif choice == "3":
        data = int(input("Enter value: "))
        pos = int(input("Enter position: "))
        sll.insert_position(data, pos)

    elif choice == "4":
        value = int(input("Enter value to delete: "))
        sll.delete_value(value)

    elif choice == "5":
        index = int(input("Enter index to delete: "))
        sll.delete_index(index)

    elif choice == "6":
        sll.display()

    elif choice == "7":
        print(Fore.MAGENTA + "Exiting program...")
        break

    else:
        print(Fore.RED + "Invalid choice. Please try again.")
