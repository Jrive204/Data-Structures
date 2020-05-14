from binary_search_tree import BSTNode


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = BSTNode(value)
            return True

    def find(self, value):
        if self.root:
            return self.root.contains(value)
        else:
            return False
