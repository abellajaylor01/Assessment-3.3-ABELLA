class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    """Left -> Root -> Right"""
    if root is None:
        return []
    return inorder(root.left) + [root.key] + inorder(root.right)


def build_jaylord_abella_tree():
    r"""
    Binary tree using JAYLORD ABELLA (13 nodes):
                 J
               /   \
              A     Y
             / \   / \
            L   O R   D
           / \ / \ / \
          A  B E L L  A
    """
    # Level 0 (Root)
    root = Node("J")

    # Level 1
    root.left = Node("A")
    root.right = Node("Y")

    # Level 2
    root.left.left = Node("L")
    root.left.right = Node("O")
    root.right.left = Node("R")
    root.right.right = Node("D")

    # Level 3
    root.left.left.left = Node("A")
    root.left.left.right = Node("B")
    root.left.right.left = Node("E")
    root.left.right.right = Node("L")
    root.right.left.left = Node("L")
    root.right.left.right = Node("A")

    return root


if __name__ == "__main__":
    tree_root = build_jaylord_abella_tree()
    print("Inorder (JAYLORD ABELLA):", " -> ".join(inorder(tree_root)))