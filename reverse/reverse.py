class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if head exists
        if self.head:
            # if we are at the end of the list
            if node.get_next() == None:
                # set new head to old last item
                self.head = node
                # close out function
                return
            # call recursively, passing in next node
            self.reverse_list(node.get_next(), node)
            # capture the next node into a value
            temp_node = node.get_next()
            # set that temp_node's pointer to the node
            temp_node.set_next(node)
            # set the head node's pointer to None
            node.set_next(None)
        else: 
            # if list is empty, it's reverse is None
            return None
