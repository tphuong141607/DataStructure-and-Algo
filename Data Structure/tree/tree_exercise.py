class TreeNode:
    def __init__(self, data):
        # self.name = name
        # self.designation = designation
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

    def print_tree_by_level(self, level):
        curr_level = self.get_level()

        if (curr_level == level): 
            return 
            
        spaces = ' ' * (3 * curr_level)
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
    
        if self.children:
            for child in self.children:
                child.print_tree_by_level(level)

        
            
            

    # def print_tree(self, type):
    #     if type == 'both': 
    #         print_type = (self.name + ' (' + self.designation + ')')
        
    #     if type == "name":
    #         print_type = self.name
        
    #     if type == "designation":
    #         print_type = self.designation

    #     level = self.get_level()
    #     spaces = ' ' * (3 * level)
    #     prefix = spaces + "|__" if self.parent else ""
    #     print(prefix + print_type)
    #     if self.children:
    #         for child in self.children:
    #             child.print_tree(type)

def build_management_tree(): 
    root = TreeNode('Anna', 'CEO')

    hr = TreeNode('Dang', 'HR Head')
    cto = TreeNode('Bill', 'CTO')
    ihead = TreeNode('ihead', 'Infrastructure Head')
    ihead.add_child(TreeNode('Infras m1', 'Infras Manager 1'))
    ihead.add_child(TreeNode('Infras m2', 'Infras Manager 2'))

    ahead = TreeNode('ahead', 'Application Head')
    ahead.add_child(TreeNode('App m1', 'App Manager 1'))
    ahead.add_child(TreeNode('App m2', 'App Manager 2'))

    cto.add_child(ihead)
    cto.add_child(ahead)

    root.add_child(cto)
    root.add_child(hr)
    return root

def build_location_tree():
    root = TreeNode("Global")
    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == '__main__':

    # Exercise 1
    # root_node = build_management_tree()
    # root_node.print_tree("name") # prints only name hierarchy
    # root_node.print_tree("designation") # prints only designation hierarchy
    # root_node.print_tree("both") # prints both (name and designation) hierarchy

    # Exercise 2
    root_node = build_location_tree()
    root_node.print_tree_by_level(3)