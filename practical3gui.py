import tkinter as tk
from tkinter import messagebox


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

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_position(self, data, pos):
        if pos == 0:
            self.insert_beginning(data)
            return True

        temp = self.head
        count = 0

        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            return False

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        return True

    def delete_value(self, value):
        if self.head is None:
            return False

        if self.head.data == value:
            self.head = self.head.next
            return True

        prev = None
        temp = self.head

        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp is None:
            return False

        prev.next = temp.next
        return True

    def delete_index(self, index):
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        prev = None
        temp = self.head
        count = 0

        while temp and count < index:
            prev = temp
            temp = temp.next
            count += 1

        if temp is None:
            return False

        prev.next = temp.next
        return True

    def display(self):
        elements = []
        temp = self.head

        while temp:
            elements.append(str(temp.data))
            temp = temp.next

        return " -> ".join(elements) if elements else "List is Empty"


sll = SinglyLinkedList()

root = tk.Tk()
root.title("Singly Linked List")
root.geometry("550x450")
root.configure(bg="#e8f4fc")

title = tk.Label(root, text="Singly Linked List Operations",
                 font=("Arial", 18, "bold"),
                 bg="#e8f4fc",
                 fg="blue")
title.pack(pady=10)

tk.Label(root, text="Value", bg="#e8f4fc",
         font=("Arial", 12)).pack()

value_entry = tk.Entry(root, font=("Arial", 12))
value_entry.pack(pady=5)

tk.Label(root, text="Position / Index", bg="#e8f4fc",
         font=("Arial", 12)).pack()

pos_entry = tk.Entry(root, font=("Arial", 12))
pos_entry.pack(pady=5)


output = tk.Label(root,
                  text="",
                  font=("Arial", 12),
                  bg="white",
                  width=55,
                  height=6,
                  relief="sunken",
                  anchor="nw",
                  justify="left")
output.pack(pady=10)


def clear():
    value_entry.delete(0, tk.END)
    pos_entry.delete(0, tk.END)


def insert_begin():
    try:
        data = int(value_entry.get())
        sll.insert_beginning(data)
        output.config(text="Inserted at Beginning")
        clear()
    except:
        messagebox.showerror("Error", "Enter a valid value")


def insert_end():
    try:
        data = int(value_entry.get())
        sll.insert_end(data)
        output.config(text="Inserted at End")
        clear()
    except:
        messagebox.showerror("Error", "Enter a valid value")


def insert_pos():
    try:
        data = int(value_entry.get())
        pos = int(pos_entry.get())

        if sll.insert_position(data, pos):
            output.config(text="Inserted Successfully")
        else:
            output.config(text="Invalid Position")

        clear()

    except:
        messagebox.showerror("Error", "Enter valid inputs")


def delete_value():
    try:
        value = int(value_entry.get())

        if sll.delete_value(value):
            output.config(text="Node Deleted")
        else:
            output.config(text="Value Not Found")

        clear()

    except:
        messagebox.showerror("Error", "Enter a valid value")


def delete_index():
    try:
        index = int(pos_entry.get())

        if sll.delete_index(index):
            output.config(text="Node Deleted")
        else:
            output.config(text="Invalid Index")

        clear()

    except:
        messagebox.showerror("Error", "Enter a valid index")


def display():
    output.config(text=sll.display())


frame = tk.Frame(root, bg="#e8f4fc")
frame.pack()

tk.Button(frame, text="Insert Beginning",
          width=18, bg="lightgreen",
          command=insert_begin).grid(row=0, column=0, padx=5, pady=5)

tk.Button(frame, text="Insert End",
          width=18, bg="lightgreen",
          command=insert_end).grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame, text="Insert Position",
          width=18, bg="lightgreen",
          command=insert_pos).grid(row=1, column=0, padx=5, pady=5)

tk.Button(frame, text="Delete Value",
          width=18, bg="tomato",
          command=delete_value).grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame, text="Delete Index",
          width=18, bg="tomato",
          command=delete_index).grid(row=2, column=0, padx=5, pady=5)

tk.Button(frame, text="Display List",
          width=18, bg="skyblue",
          command=display).grid(row=2, column=1, padx=5, pady=5)

tk.Button(root,
          text="Exit",
          width=20,
          bg="red",
          fg="white",
          command=root.destroy).pack(pady=10)

root.mainloop()
