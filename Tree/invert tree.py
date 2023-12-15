class tree:
    def __init__(self, root=0, left=None, right=None):
        self.root=root
        self.left=left
        self.right=right
    def invertTree(self, root):
        if not root:
            return None
        temp=root.left
        root.left=root.right
        root.right=temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


