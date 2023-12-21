class node:
    """
    node object for linked lis
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class SinglyLinkedList:
    """
    signly linked list implementation
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def print_list(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def insert_start(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        current_lastnode = self.head
        while current_lastnode.next:
            current_lastnode = current_lastnode.next
        current_lastnode.next = new_node

    def insert_middle(self, first_node, data):
        if first_node is None:
            return
        new_node = node(data)
        new_node.next = first_node.next
        first_node.next = new_node

    def remove_node(self, value):
        current_node = self.head
        if current_node and current_node.data == value:
            self.head = current_node.next
            return 
        prev_node = None
        while current_node and current_node.data != value:
            prev_node = current_node
            current_node = current_node.next

        if not current_node:
            return

        prev_node.next = current_node.next
