class BinarySearchTreeNode:
    def __init__(self, data): 
        self.data = data
        self.left = None 
        self.right = None 
    
    def add_child(self, data): 
        if self.data == data: 
            return 
        if data < self.data:
            # add data in left subtree
            if self.left: 
                self.left.add_child(data) 
            else: # leaf node
                self.left = BinarySearchTreeNode(data)
        else:
             # add data in left subtree
            if self.right: 
                self.right.add_child(data) 
            else: # leaf node
                self.right = BinarySearchTreeNode(data)
        
    # left subtree, node, right subtree
    # sorted from smallest to biggest
    def in_order_traversal(self): 
        elems = [] 
        if self.left:
            elems += self.left.in_order_traversal()
        
        elems.append(self.data) 

        if self.right: 
            elems += self.right.in_order_traversal()

        return elems

    # left subtree, right subtree, node 
    def post_order_traversal(self): 
        elems = [] 
        if self.left:
            elems += self.left.in_order_traversal()
        if self.right: 
            elems += self.right.in_order_traversal()
        elems.append(self.data) 

        return elems
    
     # node, left subtree, right subtree,
    def pre_order_traversal(self): 
        elems = [] 
        elems.append(self.data) 
        if self.left:
            elems += self.left.in_order_traversal()
        if self.right: 
            elems += self.right.in_order_traversal()
        
        return elems

    def search(self, val):
        if self.data == val: 
            return True 

        if val < self.data: 
            if self.left: 
                return self.left.search(val)
        else: 
            if self.right: 
                return self.right.search(val) 
        return False

    def find_max(self): 
        if self.right: 
            return self.right.find_max()

        return self.data 

    def find_min(self): 
        if self.left: 
            return self.left.find_min()

        return self.data   

    def calculate_sum(self): 
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
    # Delete a node
    # 1. Delete node with no child 
    # 2. Delete node with 1 child: change pointer 
    # 3. Delete node with 2 children: re-blance 
    #    3 Option1: take the minimum value from the right subtree and use that as the new middle node
    #    3 option2: take the maximum value from the left subtree, and use that as the new middle node

    def delete(self, val): 
        if val < self.data: 
            if self.left: 
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right: 
                self.right = self.right.delete(val)
        else: 
            # no child
            if self.left is None and self.right is None:
                return None
                
            # 1 child
            if self.left is None: 
                return self.right
            if self.right is None: 
                return self.right

            # 2 children: Option1
            # min_val = self.right.find_min()
            # self.data = min_val 
            # self.right = self.right.delete(min_val)
            
            # 2 children: Option2
            max_val = self.right.find_max()
            self.data = max_val 
            self.right = self.left.delete(max_val)

        return self

            

def build_tree(elems):
    root = BinarySearchTreeNode(elems[0])
    for i in range(1, len(elems)):
        root.add_child(elems[i])

    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.delete(34))
    print(numbers_tree.in_order_traversal())
    # print(numbers_tree.search(18))
    # print(numbers_tree.find_min())
    # print(numbers_tree.find_max())
