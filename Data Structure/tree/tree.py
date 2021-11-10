class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.children = []
        self.parent = None

    def add_child(self, child): 
        child.parent = self
        self.children.append(child)

    def get_level(self): 
        level = 0 
        curr_node = self.parent
        while curr_node: 
            level += 1
            curr_node = curr_node.parent
        return level

    def print_tree(self):
        level = self.get_level()
        spaces = ' ' * (3 * level)
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree(): 
    root = TreeNode('electronics')

    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))

    cellphone = TreeNode('Cellphone')
    cellphone.add_child(TreeNode('iPhone'))
    cellphone.add_child(TreeNode('Vivo'))

    root.add_child(laptop)
    root.add_child(cellphone)
    return root

if __name__ == "__main__":
    elect_tree = build_product_tree()
    elect_tree.print_tree()

  