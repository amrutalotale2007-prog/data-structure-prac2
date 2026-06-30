from tkinter import *
from tkinter import messagebox

class Stack:
    def __init__(self):
        self.items = []

    def insert(self, item, position):
        if position < 0 or position > len(self.items):
            raise IndexError("Invalid Position")
        self.items.insert(position, item)

    def delete(self, position):
        if position < 0 or position >= len(self.items):
            raise IndexError("Invalid Position")
        return self.items.pop(position)

    def peek(self):
        if not self.items:
            raise IndexError("Stack is Empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def traverse(self):
        if self.items:
            return " <- ".join(reversed(self.items))
        else:
            return "Stack is Empty"


stack = Stack()


def update_display():
    listbox.delete(0, END)
    for item in reversed(stack.items):
        listbox.insert(END, item)


def insert_item():
    try:
        item = entry_item.get()
        position = int(entry_position.get())

        stack.insert(item, position)
        update_display()

        entry_item.delete(0, END)
        entry_position.delete(0, END)

        messagebox.showinfo("Success", "Item Inserted Successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_item():
    try:
        position = int(entry_position.get())

        item = stack.delete(position)
        update_display()

        entry_position.delete(0, END)

        messagebox.showinfo("Deleted", f"{item} Deleted Successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def peek_item():
    try:
        messagebox.showinfo("Top Element", stack.peek())

    except Exception as e:
        messagebox.showerror("Error", str(e))


def check_empty():
    if stack.is_empty():
        messagebox.showinfo("Stack Status", "Stack is Empty")
    else:
        messagebox.showinfo("Stack Status", "Stack is Not Empty")


def stack_size():
    messagebox.showinfo("Stack Size", str(stack.size()))


def traverse_stack():
    messagebox.showinfo("Stack Traversal", stack.traverse())

root = Tk()
root.title("Stack Operations")
root.geometry("450x500")
root.configure(bg="lightblue")

title = Label(
    root,
    text="STACK OPERATIONS",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
title.pack(pady=10)

Label(root, text="Enter Item", bg="lightblue").pack()

entry_item = Entry(root, width=30)
entry_item.pack()

Label(root, text="Enter Position (0-based index)", bg="lightblue").pack()

entry_position = Entry(root, width=30)
entry_position.pack(pady=5)

Button(root, text="Insert", width=20, command=insert_item).pack(pady=5)

Button(root, text="Delete", width=20, command=delete_item).pack(pady=5)

Button(root, text="Peek", width=20, command=peek_item).pack(pady=5)

Button(root, text="Check Empty", width=20, command=check_empty).pack(pady=5)

Button(root, text="Stack Size", width=20, command=stack_size).pack(pady=5)

Button(root, text="Traverse", width=20, command=traverse_stack).pack(pady=5)

Label(
    root,
    text="Current Stack",
    font=("Arial", 12, "bold"),
    bg="lightblue"
).pack(pady=10)

listbox = Listbox(root, width=30, height=10)
listbox.pack()

root.mainloop()
