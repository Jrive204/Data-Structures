"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)
#         return self.storage

#     def pop(self):
#         if self.__len__() is 0:
#             return None
#         else:
#             return self.storage.pop()

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return self.value

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        self.current = None

    def __len__(self):
        if self.size < 0:
            self.size = 0
        return self.size

    def push(self, value):
        self.size += 1
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
            self.current = new_node

    def pop(self):
        self.size -= 1
        if not self.head:
            return None
        else:
            value = self.head
            for i in range(self.size):
                value = value.get_next()
            self.current = value.get_value()
            if self.current == self.head.get_value():
                lastValue = self.head
                self.head = None
                return lastValue.get_value()
            return value.get_value()


if __name__ == '__main__':

    i = Stack()

    i.push(100), i.__len__()
    i.push(101), i.__len__()
    i.push(105), i.__len__()
    i.push(46), i.__len__()

    print("LENGTH", i.__len__())

    # ?  1h  -->  2  -->   34   -->   55         1 -  2 -  34

    print(i.pop(), "LENGTH", i.__len__())
    print(i.pop(), "LENGTH", i.__len__())
    print(i.pop(), "LENGTH", i.__len__())
    print(i.pop(), "LENGTH", i.__len__())
    print(i.pop(), "LENGTH", i.__len__())
