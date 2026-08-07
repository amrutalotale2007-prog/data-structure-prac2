import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import heapq

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self, output):
        self.output = output

    def height(self, node):
        return node.height if node else 0

    def balance(self, node):
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):
        self.output.insert(tk.END, f"Left Rotation on {z.key}\n")
        y = z.right
        t = y.left
        y.left = z
        z.right = t
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def right_rotate(self, z):
        self.output.insert(tk.END, f"Right Rotation on {z.key}\n")
        y = z.left
        t = y.right
        y.right = z
        z.left = t
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        b = self.balance(root)

        if b > 1 and key < root.left.key:
            return self.right_rotate(root)

        if b < -1 and key > root.right.key:
            return self.left_rotate(root)

        if b > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if b < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def preorder(self, root):
        if root:
            self.output.insert(tk.END, str(root.key) + " ")
            self.preorder(root.left)
            self.preorder(root.right)


def run():
    output.delete(1.0, tk.END)

    output.insert(tk.END, "=== AVL Tree Insertion and Balancing ===\n")

    tree = AVLTree(output)
    root = None

    values = [20, 4, 15, 70, 50, 100, 80]

    for v in values:
        output.insert(tk.END, f"Inserting {v}...\n")
        root = tree.insert(root, v)

    output.insert(tk.END, "\nAVL Tree Pre-Order Traversal:\n")
    tree.preorder(root)

    output.insert(tk.END, "\n\n=== Heap Examples ===\n")

    data = [9, 5, 6, 2, 3]

    min_heap = data.copy()
    heapq.heapify(min_heap)
    output.insert(tk.END, f"Min-Heap: {min_heap}\n")

    max_heap = [-x for x in data]
    heapq.heapify(max_heap)
    output.insert(tk.END, f"Max-Heap: {[-x for x in max_heap]}\n")

    output.insert(tk.END, "\n=== Task Manager using Priority Queue ===\n")

    pq = []
    heapq.heappush(pq, (2, "Low priority: Backup database"))
    heapq.heappush(pq, (1, "High priority: Handle emergency patient"))
    heapq.heappush(pq, (3, "Medium priority: Run diagnostics"))

    output.insert(tk.END, "\nProcessing Tasks by Priority:\n")

    while pq:
        p, task = heapq.heappop(pq)
        output.insert(tk.END, f"Priority {p} -> Task: {task}\n")


root = tk.Tk()
root.title("AVL Tree, Heap and Priority Queue")
root.geometry("850x650")
root.configure(bg="white")

title = tk.Label(root,
                 text="AVL Tree, Heap and Priority Queue Simulation",
                 font=("Arial", 18, "bold"),
                 bg="white",
                 fg="blue")
title.pack(pady=10)

btn = tk.Button(root,
                text="Run Simulation",
                font=("Arial", 12, "bold"),
                bg="green",
                fg="white",
                command=run)
btn.pack(pady=5)

output = ScrolledText(root,
                      width=95,
                      height=30,
                      font=("Consolas", 11))
output.pack(padx=10, pady=10)

root.mainloop()
