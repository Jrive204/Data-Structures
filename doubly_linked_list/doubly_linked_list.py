"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        # print(self.value, "Inside Insert After")
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev  # NONE
        # print(self.value, "Inside Insert before")
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            print("in prev")
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            print("in next", self.next.prev)


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        if self.head is None:
            self.__init__(node=ListNode(value))
            return
        else:
            self.length += 1
            self.head.insert_before(value)
            # print(self.head.prev.value, "test")
            self.head = self.head.prev

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if self.length == 0:
            return None
        else:
            self.length -= 1
            if self.length == 0:
                lastval = self.head
                self.head = None
                self.tail = None
                return lastval.value
            self.head.delete()
            self.head = self.head.next
            print(self.tail.value, "ERROR")

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if self.head is None:
            current_head = self.__init__(node=ListNode(value))
            return
        else:
            self.length += 1
            self.tail.insert_after(value)
            self.tail = self.tail.next
            print(self.tail.value, "what are you")

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.length == 0:
            return None
        else:
            self.length -= 1
            if self.length == 0:
                lastval = self.tail
                self.head = None
                self.tail = None
                return lastval.value
            self.tail.delete()
            self.tail = self.tail.prev

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return None
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return None
        value = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # check if the node is the head
        elif self.head is node:
            self.head = node.next
            node.delete()
        # check if the node is the tail
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        # otherwise, there's no additional references we need to update
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        current_max = self.head.value
        current = self.head.next
        while current is not None:
            if current.value > current_max:
                current_max = current.value
            current = current.next
        return current_max


a = DoublyLinkedList()

a.add_to_tail(1)
a.add_to_tail(2)
a.add_to_tail(5)
# a.remove_from_tail()
print("TAIL VALUE", a.tail.value, "TAIL prev Value:", a.tail.prev.value)
print("Head Value:", a.head.value, "Head next Value:", a.head.next.value)
# ? 1h <= => 2 =>  <= 5t

# print(a.tail.value, "REMOVE5")
a.remove_from_tail()
a.remove_from_tail()
a.remove_from_tail()
a.remove_from_tail()
a.remove_from_tail()

# print(a.tail.value, "REMOVE2")

# print(a.__len__(), "Length")

# print(a.tail.value, "REMOVE1")
# a.remove_from_tail()

# print(a.__len__(), "Length")

# # print(a.head.value, "head")

# print(a.__len__(), "Length")
