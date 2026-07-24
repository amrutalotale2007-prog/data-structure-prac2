import tkinter as tk
from tkinter import messagebox, simpledialog


class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            return "Queue is full. Cannot enqueue."
        self.queue.append(item)
        return f"Enqueued: {item}"

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty. Cannot dequeue."
        item = self.queue.pop(0)
        return f"Dequeued: {item}"

    def peek(self):
        if self.is_empty():
            return "Queue is empty."
        return f"Front of the Queue: {self.queue[0]}"

    def traverse(self):
        if self.is_empty():
            return "Queue is empty."
        return " -> ".join(map(str, self.queue))


class QueueGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue Operations")
        self.root.geometry("500x500")
        self.root.configure(bg="lightblue")

        max_size = simpledialog.askinteger(
            "Queue Size",
            "Enter Maximum Queue Size:",
            minvalue=1
        )

        if max_size is None:
            root.destroy()
            return

        self.queue = Queue(max_size)

        title = tk.Label(
            root,
            text="QUEUE OPERATIONS",
            font=("Arial", 18, "bold"),
            bg="lightblue",
            fg="darkblue"
        )
        title.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        tk.Button(root, text="Enqueue", width=20, command=self.enqueue).pack(pady=5)
        tk.Button(root, text="Dequeue", width=20, command=self.dequeue).pack(pady=5)
        tk.Button(root, text="Peek", width=20, command=self.peek).pack(pady=5)
        tk.Button(root, text="Traverse", width=20, command=self.traverse).pack(pady=5)
        tk.Button(root, text="Display Queue", width=20, command=self.display).pack(pady=5)
        tk.Button(root, text="Check Empty", width=20, command=self.check_empty).pack(pady=5)
        tk.Button(root, text="Check Full", width=20, command=self.check_full).pack(pady=5)
        tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=5)

        self.output = tk.Text(root, height=10, width=50, font=("Arial", 12))
        self.output.pack(pady=10)

    def show_output(self, message):
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, message)

    def enqueue(self):
        item = self.entry.get()
        if item == "":
            messagebox.showwarning("Warning", "Please enter an item.")
            return
        result = self.queue.enqueue(item)
        self.show_output(result)
        self.entry.delete(0, tk.END)

    def dequeue(self):
        self.show_output(self.queue.dequeue())

    def peek(self):
        self.show_output(self.queue.peek())

    def traverse(self):
        self.show_output(self.queue.traverse())

    def display(self):
        if self.queue.is_empty():
            self.show_output("Queue is empty.")
        else:
            text = "Current Queue:\n"
            for i, item in enumerate(self.queue.queue, start=1):
                text += f"{i}. {item}\n"
            self.show_output(text)

    def check_empty(self):
        if self.queue.is_empty():
            self.show_output("Queue is Empty.")
        else:
            self.show_output("Queue is Not Empty.")

    def check_full(self):
        if self.queue.is_full():
            self.show_output("Queue is Full.")
        else:
            self.show_output("Queue is Not Full.")


if __name__ == "__main__":
    root = tk.Tk()
    app = QueueGUI(root)
    root.mainloop()
