class TreeNode:
    """Node class for a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """Binary tree implementation."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the binary tree."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        """Helper method to insert a value recursively."""
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def in_order_traversal(self):
        """Perform in-order traversal (left, root, right)."""
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        """Helper method for in-order traversal."""
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.value)  # Visit the node
            self._in_order_recursive(node.right, result)

    def pre_order_traversal(self):
        """Perform pre-order traversal (root, left, right)."""
        result = []
        self._pre_order_recursive(self.root, result)
        return result

    def _pre_order_recursive(self, node, result):
        """Helper method for pre-order traversal."""
        if node:
            result.append(node.value)  # Visit the node
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)

    def post_order_traversal(self):
        """Perform post-order traversal (left, right, root)."""
        result = []
        self._post_order_recursive(self.root, result)
        return result

    def _post_order_recursive(self, node, result):
        """Helper method for post-order traversal."""
        if node:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.value)

# Example usage
if __name__ == "__main__":
    tree = BinaryTree()

    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(12)
    tree.insert(18)

    print("In-order traversal:", tree.in_order_traversal())
    print("Pre-order traversal:", tree.pre_order_traversal())
    print("Post-order traversal:", tree.post_order_traversal())
