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


def build_huffman_tree(text):
    freq = Counter(text)
    print("Starting Huffman Encoding...")
    print("Character Frequencies:", dict(freq))
    print()

    heap = []

    for ch, f in sorted(freq.items()):
        heapq.heappush(heap, Node(ch, f))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        print(f"Merging nodes: {left.char} ({left.freq}) and {right.char} ({right.freq})")

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, code="", codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = code
        print(f"Assigning code to character {node.char}: {code}")

    generate_codes(node.left, code + "0", codes)
    generate_codes(node.right, code + "1", codes)

    return codes


def encode(text, codes):
    encoded = "".join(codes[ch] for ch in text)
    print("\nEncoded Data:", encoded)
    print("Encoding completed!")
    print()
    print("Codebook:", codes)
    return encoded


def decode(encoded, root):
    print("\nStarting Huffman Decoding...\n")

    decoded = ""
    current = root
    bits = ""

    for bit in encoded:
        bits += bit

        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            print(f"Decoding: {bits} -> {current.char}")
            decoded += current.char
            bits = ""
            current = root

    print("\nDecoding completed!")
    return decoded


def main():
    print("Welcome to Huffman Coding CLI Application!")

    text = input("Enter the text to encode: ")

    if not text:
        print("Input cannot be empty!")
        return

    root = build_huffman_tree(text)

    codes = generate_codes(root, "", {})

    encoded = encode(text, codes)

    decoded = decode(encoded, root)

    print("\nOriginal data:", text)
    print("Decoded data:", decoded)

    if text == decoded:
        print("\nSuccess: The original and decoded data match!")
    else:
        print("\nError: Decoding failed!")


if __name__ == "__main__":
    main()
