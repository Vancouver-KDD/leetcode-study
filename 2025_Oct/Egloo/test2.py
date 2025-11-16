class Node():
    def __init__(self, value, timestamp):
        self.value = value
        self.timestamp = timestamp
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.head = None

    def travel(self):
        self.travel_helper(self.head)

    def travel_helper(self, node):
        if node == None:
            return
        self.travel_helper(node.left)
        print(node.value)
        self.travel_helper(node.right)

    def add(self, value, timestamp):
        if not self.head:
            self.head = Node(value, timestamp)
            return

        node = self.head
        while True:
            if timestamp <= node.timestamp:
                if not node.left:
                    node.left = Node(value, timestamp)
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = Node(value, timestamp)
                    break
                else:
                    node = node.right

    def search(self, timestamp):
        node = self.head
        prev = ""

        while node:
            if node.timestamp == timestamp:
                return node.value
            elif node.timestamp < timestamp:
                prev = node.value
                node = node.right
            else:
                node = node.left
        return prev

arr = [6,23,1,2,7,8,10,15,19]

b = BST()
for a in arr:
    b.add(str(a), a)

b.travel()
print("---- search ----")
print(6, b.search(6))
print(1, b.search(1))
print(9, b.search(9))
print(18, b.search(18))

