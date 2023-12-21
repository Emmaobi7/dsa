class Stack():
    """
    stack data strcture
    """
    def __init__(self):
        self.stack = []

    def peek(self):
        """"
        peek: get top-most element in stack
        """
        if self.stack:
            return self.stack[-1]
        return ('stack is empty')

    def add(self, data):
        """
        add: (push) add to stack
        """
        if data not in self.stack:
            return self.stack.append(data)

    def remove(self):
        """
        remove: pop stack
        """
        if len(self.stack) <= 0:
            return ('stack is empty')
        else:
            return self.stack.pop()
