from tkinter import *
from tkinter import messagebox, simpledialog

class PriorityQueue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item, priority):
        if len(self.queue) >= self.size:
            messagebox.showerror("Error", "Queue is Full")
            return
        self.queue.append((priority, item))
        self.queue.sort()

    def dequeue(self):
        if not self.queue:
            messagebox.showerror("Error", "Queue is Empty")
            return
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def ascending(self):
        return self.queue

    def descending(self):
        return sorted(self.queue, reverse=True)

 
size = simpledialog.askinteger("Queue Size", "Enter Queue Capacity:")
pq = PriorityQueue(size)

root = Tk()
root.title("Priority Queue")
root.geometry("500x450")

display = Text(root, width=50, height=15)
display.pack(pady=10)


def show(data):
    display.delete(1.0, END)
    if not data:
        display.insert(END, "Queue is Empty")
    else:
        for p, i in data:
            display.insert(END, f"Item: {i}   Priority: {p}\n")


def enqueue():
    item = simpledialog.askstring("Item", "Enter Item:")
    priority = simpledialog.askinteger("Priority", "Enter Priority:")
    if item is not None and priority is not None:
        pq.enqueue(item, priority)
        show(pq.ascending())


def dequeue():
    item = pq.dequeue()
    if item:
        messagebox.showinfo("Dequeued", f"Item: {item[1]}")
        show(pq.ascending())


def traverse():
    show(pq.ascending())


def empty():
    if pq.is_empty():
        messagebox.showinfo("Status", "Queue is Empty")
    else:
        messagebox.showinfo("Status", "Queue is Not Empty")


def full():
    if pq.is_full():
        messagebox.showinfo("Status", "Queue is Full")
    else:
        messagebox.showinfo("Status", "Queue is Not Full")


def ascending():
    show(pq.ascending())


def descending():
    show(pq.descending())


Button(root, text="Enqueue", width=15, command=enqueue).pack(pady=2)
Button(root, text="Dequeue", width=15, command=dequeue).pack(pady=2)
Button(root, text="Traverse", width=15, command=traverse).pack(pady=2)
Button(root, text="Is Empty", width=15, command=empty).pack(pady=2)
Button(root, text="Is Full", width=15, command=full).pack(pady=2)
Button(root, text="Ascending", width=15, command=ascending).pack(pady=2)
Button(root, text="Descending", width=15, command=descending).pack(pady=2)
Button(root, text="Exit", width=15, command=root.destroy).pack(pady=5)

root.mainloop()
