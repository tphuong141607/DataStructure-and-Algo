class Node: 
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def get_length(self): 
        count = 0
        curr_node = self.head 
        while curr_node:
            count += 1
            curr_node = curr_node.next 
        return count

    def insert_at_beginning(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        curr_node = self.head 
        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = Node(data, None, curr_node)
    
    def insert_at(self, index, data): 
        if index < 0 or index >= self.get_length(): 
            raise Exception("Invalid index") 
        if index == 0: 
            self.insert_at_beginning(data)
            return 
    
        count = 0 
        curr_node = self.head

        while (curr_node): 
            if (count == index - 1): 
                new_node = Node(data, curr_node.next, curr_node)
                if curr_node.next:
                    curr_node.next.prev = new_node
                curr_node.next = new_node
                return 
            curr_node = curr_node.next
            count += 1 

    def insert_after_value(self, value, data_to_insert):
        if self.head is None:
            return

        curr_node = self.head 
        while(curr_node):
            if (curr_node.data == value): 
                new_node = Node(data_to_insert, curr_node.next, curr_node)    
                if curr_node.next: 
                    curr_node.next.prev = new_node
                curr_node.next = new_node
                return 

            curr_node = curr_node.next

    # Create a new linked list for the given list 
    def insert_values(self, data_list): 
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def remove_by_value(self, data):
        if self.head is None:
            return
            
        if (self.head.data == data): 
            self.head = self.head.next
            self.head.prev = None 
            return 

        curr_node = self.head 
        while(curr_node.next):
            if (curr_node.next.data == data): 
                if (curr_node.next.next):  
                    curr_node.next.next.prev = curr_node
                curr_node.next = curr_node.next.next    
                return 

            curr_node = curr_node.next

    def remove_at(self, index): 
        if index < 0 or index >= self.get_length(): 
            raise Exception("Invalid index") 
        if index == 0: 
            self.head = self.head.next
            self.head.prev = None
            return 

        count = 0 
        curr_node = self.head 
        while curr_node:
            if (count == index - 1): 
                if (curr_node.next.next):  
                    curr_node.next.next.prev = curr_node
                curr_node.next = curr_node.next.next    
                return 

            curr_node = curr_node.next
            count += 1 

    def print(self): 
        if (self.head is None): 
            print('Linked list is empty') 
            return
        
        curr_node = self.head 
        linkedlist_str = ''
        while curr_node: 
            linkedlist_str += str(curr_node.data) + ' <---> ' 
            curr_node = curr_node.next
        linkedlist_str += 'None'
        print(linkedlist_str)
    
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        curr_node = self.head
        linkedlist_str = ''
        while curr_node:
            linkedlist_str += str(curr_node.data) + ' --> '
            curr_node = curr_node.next
        print(linkedlist_str)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + ' --> '
            itr = itr.prev
        print("Link list in reverse: ", llstr)

if __name__ == '__main__':
    # ll = LinkedList();
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    # ll.insert_at_end(99)
    # ll.insert_at_end(59)
    # ll.print()
    
    ll2 = LinkedList() 
    ll2.insert_values(['banana', 'orange', 'coconut', 'blueberry', 'mango'])
    ll2.print()
    ll2.insert_at(3, 'watermelon')
    ll2.print()
    ll2.insert_after_value('banana', 'papaya')
    ll2.print()
    ll2.remove_by_value('mango')
    ll2.print()
    ll2.remove_at(2)
    ll2.print()


    # ll3 = LinkedList() 
    # ll3.print()
   