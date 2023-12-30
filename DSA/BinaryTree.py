class BinaryTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def populate(self):
        value = int(input("Enter the root Node: "))
        self.root = self.Node(value)
        self.populate_helper(self.root)

    def populate_helper(self, node):
        left = input(f"Do you want to enter left of {node.value}? (True/False): ").lower() == 'true'
        if left:
            value = int(input(f"Enter the value of the left of {node.value}: "))
            node.left = self.Node(value)
            self.populate_helper(node.left)

        right = input(f"Do you want to enter right of {node.value}? (True/False): ").lower() == 'true'
        if right:
            value = int(input(f"Enter the value of the right of {node.value}: "))
            node.right = self.Node(value)
            self.populate_helper(node.right)

    def display(self):
        self.display_helper(self.root, "")
    def display_helper(self, node, indent):
        if node is None:
            return
        print(indent + str(node.value))
        self.display_helper(node.left, indent + "\t")
        self.display_helper(node.right, indent + "\t")
    
    def pretty_display(self):
        self.pretty_display_helper(self.root, 0)
    def pretty_display_helper(self, node, level):
        if node is None:
            return
        self.pretty_display_helper(node.right, level + 1)
        if level != 0:
            for i in range(level - 1):
                print("|      ", end="")
            print("|------->" + str(node.value))
        else:
            print(node.value)

        self.pretty_display_helper(node.left, level + 1)

    def pre_order(self):
        self.pre_order_helper(self.root)
    def pre_order_helper(self, node):
        if node is None:
            return
        print(node.value, end=" ")
        self.pre_order_helper(node.left)
        self.pre_order_helper(node.right)

    def in_order(self):
        self.in_order_helper(self.root)
    def in_order_helper(self, node):
        if node is None:
            return
        self.in_order_helper(node.left)
        print(node.value, end=" ")
        self.in_order_helper(node.right)

    def post_order(self):
        self.post_order_helper(self.root)
    def post_order_helper(self, node):
        if node is None:
            return
        self.post_order_helper(node.left)
        self.post_order_helper(node.right)
        print(node.value, end=" ")


tree = BinaryTree()
tree.populate()
print("\nDisplaying the tree:")
tree.display()
print("\nPretty Display of the tree:")
tree.pretty_display()
print("\nPre-order Traversal:")
tree.pre_order()
print("\nIn-order Traversal:")
tree.in_order()
print("\nPost-order Traversal:")
tree.post_order()
