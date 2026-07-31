from colorama import init, Fore

init(autoreset=True)

class PriorityQueue:
    def __init__(self, size):
        self.q = []
        self.size = size

    def enqueue(self, item, priority):
        if len(self.q) == self.size:
            print(Fore.RED + "Queue is Full")
        else:
            self.q.append((priority, item))
            self.q.sort()
            print(Fore.GREEN + "Item Enqueued")

    def dequeue(self):
        if not self.q:
            print(Fore.RED + "Queue is Empty")
        else:
            print(Fore.GREEN + f"Dequeued: {self.q.pop(0)[1]}")

    def traverse(self):
        if not self.q:
            print(Fore.YELLOW + "Queue is Empty")
        else:
            for p, i in self.q:
                print(f"Item: {i}, Priority: {p}")

    def is_empty(self):
        print("Queue is Empty" if not self.q else "Queue is Not Empty")

    def is_full(self):
        print("Queue is Full" if len(self.q) == self.size else "Queue is Not Full")

    def ascending(self):
        for p, i in sorted(self.q):
            print(f"Item: {i}, Priority: {p}")

    def descending(self):
        for p, i in sorted(self.q, reverse=True):
            print(f"Item: {i}, Priority: {p}")

def main():
    pq = PriorityQueue(int(input("Enter Queue Size: ")))

    while True:
        print("\n1.Enqueue\n2.Dequeue\n3.Traverse\n4.Is Empty")
        print("5.Is Full\n6.Ascending\n7.Descending\n8.Exit")

        ch = input("Enter Choice: ")

        if ch == "1":
            item = input("Enter Item: ")
            priority = int(input("Enter Priority: "))
            pq.enqueue(item, priority)

        elif ch == "2":
            pq.dequeue()

        elif ch == "3":
            pq.traverse()

        elif ch == "4":
            pq.is_empty()

        elif ch == "5":
            pq.is_full()

        elif ch == "6":
            pq.ascending()

        elif ch == "7":
            pq.descending()

        elif ch == "8":
            print("Exiting...")
            break

        else:
            print(Fore.RED + "Invalid Choice")

if __name__ == "__main__":
    main()
