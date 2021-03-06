class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return repr(self.data)
    
    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node


def create_tree():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    nine.add_right(eight)
    three = Node(3)
    four = Node(4)
    eight.add_left(three)
    eight.add_right(four)
    # now return the root node
    return two

root = create_tree()

stack = []
stack.append(root)

while stack:
    node = stack.pop()
    print(node)

    # pre order Root-L-R
    # LIFO - left will be first pop()
    if node.right:
        stack.append(node.right)

    if node.left:
        stack.append(node.left)
