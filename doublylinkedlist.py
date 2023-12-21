class Node():
    """
    doubly linked list node
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)


class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def print_list(self, node):
        while node is not None:
            print(node.data)
            track_last = node
            node = node.next
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert(self, prev_node, data):
        if prev_node is None:
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node


    def append(self, data):
        new_node = Node(data)
        new_node.next = None
        if self.head is None:
            return self.push(data)
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return
