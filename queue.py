import collections

class Queue():
    """
    queue data starucutre
    """
    def __init__(self):
        self.queue = collections.deque()

    def size(self):
        """
        return size of queue
        """
        return len(self.queue)

    def add(self, data):
        """
        add to queue data structure
        """
        if data not in self.queue:
            return self.queue.append(data)
        
    def remove(self):
        if len(self.queue) <= 0:
            return
        return self.queue.popleft()


