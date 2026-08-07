import heapq

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:

    def height(self, node):
        return node.height if node else 0

    def balance(self, node):
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):
        print(f"Left Rotation on {z.key}")
        y = z.right
        t = y.left
        y.left = z
        z.right = t

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def right_rotate(self, z):
        print(f"Right Rotation on {z.key}")
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
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

print("=== AVL Tree Insertion and Balancing ===")

tree = AVLTree()
root = None

values = [20, 4, 15, 70, 50, 100, 80]

for v in values:
    print(f"Inserting {v}...")
    root = tree.insert(root, v)

print("\n\nAVL Tree Pre-Order Traversal:")
tree.preorder(root)

print("\n\n=== Heap Examples ===")

data = [9, 5, 6, 2, 3]

min_heap = data.copy()
heapq.heapify(min_heap)
print("Min-Heap:", min_heap)

max_heap = [-x for x in data]
heapq.heapify(max_heap)
print("Max-Heap:", [-x for x in max_heap])

print("\n\n=== Task Manager using Priority Queue ===")

pq = []
heapq.heappush(pq, (2, "Low priority: Backup database"))
heapq.heappush(pq, (1, "High priority: Handle emergency patient"))
heapq.heappush(pq, (3, "Medium priority: Run diagnostics"))

print("\nProcessing Tasks by Priority:")

while pq:
    p, task = heapq.heappop(pq)
    print(f"Priority {p} -> Task: {task}")
