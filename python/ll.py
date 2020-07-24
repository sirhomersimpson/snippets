## https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LL:

    def __init__(self):
        self.head = None

    def insert_in_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_node(self, key):
        pass

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next

### main code
ll = LL()
ll.insert_in_front(20)
ll.insert_in_front(30)
ll.insert_in_front(50)
ll.insert_in_front(60)

ll.print_list()