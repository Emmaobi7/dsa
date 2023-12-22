class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    def print_tree(self):
        """
        in-order printing
        """
        if self.left:
            self.left.print_tree()

        print(self.data)

        if self.right:
            self.right.print_tree()


    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    
    def inorder(self, root):
        """
        inorder traversal
        """
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)

        return res

    def preorder(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res


    def postorder(self, root):
        res = []
        if root:
            res = self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.data)
        return res
