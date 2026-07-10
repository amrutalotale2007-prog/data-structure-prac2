import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)

        if self.head:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_position(self, pos, data):
        if pos == 1:
            self.insert_begin(data)
            return

        temp = self.head
        count = 1

        while temp and count < pos - 1:
            temp = temp.next
            count += 1

        if not temp:
            return False

        new_node = Node(data)

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node
        return True

    def delete_begin(self):
        if not self.head:
            return False

        self.head = self.head.next

        if self.head:
            self.head.prev = None

        return True

    def delete_end(self):
        if not self.head:
            return False

        if not self.head.next:
            self.head = None
            return True

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None
        return True

    def delete_position(self, pos):
        if not self.head:
            return False

        if pos == 1:
            return self.delete_begin()

        temp = self.head
        count = 1

        while temp and count < pos:
            temp = temp.next
            count += 1

        if not temp:
            return False

        if temp.next:
            temp.next.prev = temp.prev

        temp.prev.next = temp.next
        return True

    def search(self, key):
        temp = self.head
        pos = 1

        while temp:
            if temp.data == key:
                return pos

            temp = temp.next
            pos += 1

        return -1

    def display(self):
        result = []
        temp = self.head

        while temp:
            result.append(str(temp.data))
            temp = temp.next

        return " <-> ".join(result)

    def length(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count


dll = DoublyLinkedList()

def update_display():
    display_box.delete("1.0", tk.END)
    display_box.insert(tk.END, dll.display())


def insert_begin():
    try:
        data = int(data_entry.get())
        dll.insert_begin(data)
        update_display()
    except:
        messagebox.showerror("Error", "Enter valid number")


def insert_end():
    try:
        data = int(data_entry.get())
        dll.insert_end(data)
        update_display()
    except:
        messagebox.showerror("Error", "Enter valid number")


def insert_pos():
    try:
        data = int(data_entry.get())
        pos = int(pos_entry.get())

        if dll.insert_position(pos, data) == False:
            messagebox.showerror("Error", "Invalid Position")

        update_display()

    except:
        messagebox.showerror("Error", "Enter valid values")


def delete_begin():
    dll.delete_begin()
    update_display()


def delete_end():
    dll.delete_end()
    update_display()


def delete_pos():
    try:
        pos = int(pos_entry.get())

        if dll.delete_position(pos) == False:
            messagebox.showerror("Error", "Invalid Position")

        update_display()

    except:
        messagebox.showerror("Error", "Enter valid position")


def search_node():
    try:
        key = int(data_entry.get())
        result = dll.search(key)

        if result == -1:
            messagebox.showinfo("Search", "Element Not Found")
        else:
            messagebox.showinfo("Search", f"Found at Position {result}")

    except:
        messagebox.showerror("Error", "Enter valid value")


def show_length():
    messagebox.showinfo("Length", f"Length = {dll.length()}")


root = tk.Tk()
root.title("Doubly Linked List GUI")
root.geometry("700x500")
root.configure(bg="lightblue")

title = tk.Label(
    root,
    text="DOUBLY LINKED LIST OPERATIONS",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
title.pack(pady=10)

tk.Label(root, text="Data:", bg="lightblue").pack()
data_entry = tk.Entry(root)
data_entry.pack()

tk.Label(root, text="Position:", bg="lightblue").pack()
pos_entry = tk.Entry(root)
pos_entry.pack()

frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=10)

tk.Button(frame, text="Insert Begin", command=insert_begin).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Insert End", command=insert_end).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Insert Position", command=insert_pos).grid(row=0, column=2, padx=5, pady=5)

tk.Button(frame, text="Delete Begin", command=delete_begin).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Delete End", command=delete_end).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame, text="Delete Position", command=delete_pos).grid(row=1, column=2, padx=5, pady=5)

tk.Button(frame, text="Search", command=search_node).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame, text="Length", command=show_length).grid(row=2, column=1, padx=5, pady=5)

display_box = tk.Text(root, height=10, width=60)
display_box.pack(pady=20)

root.mainloop()
