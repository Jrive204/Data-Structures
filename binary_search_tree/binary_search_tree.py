"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if self.value == value:
        #     print(self.value, "TESTING 1")
        #     return False
        if self.value > value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
                return True
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)
                return True

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False
    # Return the maximum value found in the tree

    def get_max(self):
        if self.right is None:
            # The Break case if there is not a value to the right.
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
     # Applies the function to the node.
        fn(self.value)
        # If there is a left value, run the for_each passing in the
        # function.
        if self.left:
            self.left.for_each(fn)
        # If there is a right value, run the for_each passing in the
        # function.
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque()

        # add the root node
        queue.append(node)

        # loop so long as the stack still has elements
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            print(int(current.value))

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        if node:
            print(node.value)

            self.dft_print(node.left)

            self.dft_print(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# print(bst.value)
# print(bst.right.value)
# print(bst.right.value, "NODE")
bst.bft_print(bst)

# bst.insert(10)
# bst.insert(2)
# bst.insert(11)
# bst.insert(10)
# bst.insert(10)


# print(bst.value)
# print(bst.left.value)
# print(bst.right.value)
# print(bst.right.right.value)
