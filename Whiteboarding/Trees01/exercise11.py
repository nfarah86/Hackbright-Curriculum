class BinaryTreeNode:
    def __init__(self, root):
        self.left = None
        self.right = None
        self.root = root

    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def insert_left(self, newNode):
        tree = BinaryTreeNode(newNode)
        if self.left == None:
            self.left = tree
        else:
            self.left = tree
            tree.left = self.left

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node

    def insert_right(self, newNode):
        tree = BinaryTreeNode(newNode)
        if self.right == None:
            self.right = tree
        else:
            tree.right = self.right
            self.right = tree

    def get_value(self):
        return self.root

    def set_value(self, newRoot):
        self.root = newRoot

def print_Tree(tree):
    if tree != None:
        print_Tree(tree.get_left())
        print(tree.get_value())
        print_Tree(tree.get_right())


def depth_first_traversal(node):
    pass


tempBTN = BinaryTreeNode(3)
tempBTN.insert_left("bob")
tempBTN.insert_right("karen")
print_Tree(tempBTN)
