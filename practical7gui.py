import tkinter as tk
from tkinter import messagebox
import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.freq == other.freq:
            return (self.char or "") < (other.char or "")
        return self.freq < other.freq


class HuffmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Huffman Coding GUI")
        self.root.geometry("850x700")
        self.root.configure(bg="white")

        self.codes = {}
        self.root_node = None

        title = tk.Label(root,
                         text="Huffman Coding GUI Application",
                         font=("Arial", 20, "bold"),
                         bg="white",
                         fg="blue")
        title.pack(pady=10)

        frame = tk.Frame(root, bg="white")
        frame.pack()

        tk.Label(frame, text="Enter Text:",
                 font=("Arial", 12),
                 bg="white").grid(row=0, column=0, padx=5)

        self.entry = tk.Entry(frame, width=40, font=("Arial", 12))
        self.entry.grid(row=0, column=1, padx=5)

        tk.Button(frame,
                  text="Encode",
                  bg="green",
                  fg="white",
                  font=("Arial", 11, "bold"),
                  command=self.encode_text).grid(row=0, column=2, padx=5)

        tk.Button(frame,
                  text="Clear",
                  bg="red",
                  fg="white",
                  font=("Arial", 11, "bold"),
                  command=self.clear).grid(row=0, column=3, padx=5)

        self.output = tk.Text(root,
                              width=100,
                              height=35,
                              font=("Consolas", 11))
        self.output.pack(pady=15)

    def build_tree(self, text):
        freq = Counter(text)

        self.output.insert(tk.END, "Starting Huffman Encoding...\n")
        self.output.insert(tk.END, f"Character Frequencies: {dict(freq)}\n\n")

        heap = []

        for ch, f in sorted(freq.items()):
            heapq.heappush(heap, Node(ch, f))

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            self.output.insert(
                tk.END,
                f"Merging nodes: {left.char} ({left.freq}) and {right.char} ({right.freq})\n"
            )

            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

        return heap[0]

    def generate_codes(self, node, code=""):
        if node is None:
            return

        if node.char is not None:
            self.codes[node.char] = code
            self.output.insert(
                tk.END,
                f"Assigning code to character {node.char}: {code}\n")

        self.generate_codes(node.left, code + "0")
        self.generate_codes(node.right, code + "1")

    def decode(self, encoded):
        self.output.insert(tk.END, "\nStarting Huffman Decoding...\n\n")

        decoded = ""
        current = self.root_node
        bits = ""

        for bit in encoded:
            bits += bit

            if bit == "0":
                current = current.left
            else:
                current = current.right

            if current.char is not None:
                self.output.insert(
                    tk.END,
                    f"Decoding: {bits} -> {current.char}\n")
                decoded += current.char
                bits = ""
                current = self.root_node

        self.output.insert(tk.END, "\nDecoding completed!\n")
        return decoded

    def encode_text(self):
        self.output.delete(1.0, tk.END)

        text = self.entry.get()

        if text == "":
            messagebox.showerror("Error", "Please enter text.")
            return

        self.codes = {}

        self.root_node = self.build_tree(text)

        self.generate_codes(self.root_node)

        encoded = ""

        for ch in text:
            encoded += self.codes[ch]

        self.output.insert(tk.END, "\nEncoded Data: " + encoded + "\n")
        self.output.insert(tk.END, "Encoding completed!\n\n")

        self.output.insert(tk.END, "Codebook:\n")

        for ch in sorted(self.codes):
            self.output.insert(
                tk.END,
                f"{ch} : {self.codes[ch]}\n")

        decoded = self.decode(encoded)

        self.output.insert(tk.END, "\nOriginal Data : " + text + "\n")
        self.output.insert(tk.END, "Decoded Data  : " + decoded + "\n\n")

        if decoded == text:
            self.output.insert(
                tk.END,
                "SUCCESS: Original and Decoded data match!\n")
        else:
            self.output.insert(
                tk.END,
                "ERROR: Decoding failed!\n")

    def clear(self):
        self.entry.delete(0, tk.END)
        self.output.delete(1.0, tk.END)


root = tk.Tk()
app = HuffmanGUI(root)
root.mainloop()
