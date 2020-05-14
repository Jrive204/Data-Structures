class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'Current value: {self.value}'


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(value=nodes.pop(0))
            self.head = node
            for i in nodes:
                node.next = Node(value=i)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            print(nodes, 'Node[]')
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node, new_node):
        if not self.head:
            raise Exception("list is Empty")

        for node in self:
            if node.value == target_node:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"node with data '{target_node}' not found")

    def add_before(self, target_node, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.value == target_node:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.value == target_node:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with value '%s' not found" % target_node)

    def remove_node(self, target_node):
        if not self.head:
            raise Exception("List is Empty")

        if self.head.value == target_node:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.value == target_node:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f"Node with Data {target_node} not found")


# alphaList = ["1", "2", "3", "4", "5"]

# llist = LinkedList(["a", "b", "c", "d", "e"])
llist = LinkedList()
llist.add_first(Node('c'))

llist.add_first(Node('b'))
# llist.add_last(Node(55))
# llist.add_last(Node('a'))
llist.add_last(Node('z'))
llist.add_last(Node('Y'))

llist.add_after("b", Node("J"))
llist.add_before("J", Node("12"))


print(llist)

# for node in llist:
#     print(node)
