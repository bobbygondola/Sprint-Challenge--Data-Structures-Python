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

    """ 
    
    RECURSIVELY RUN THROUGH ALL,
    UNTIL NO MORE,
    SET NEXT AS PREV,
    REVERSED
    
    RUNTIME O(logn)
    
    """
    
    def reverse_list(self, node, prev):
        if self.head is None:               # IF EMPTY
            return None
        elif node.next_node:                    #IF NEXT EXISTS
            new_node = node.get_next()              # SET NEW_NODE TO THE NEXT ONE
            self.reverse_list(new_node, node)           # RESET FUNCTION
        else:                                   # IF NEXT DOESNT EXIST( aka end ),
            self.head = node                        # SET HEAD AS NODE
        node.set_next(prev)                     # ONCE WENT THROUGH ALL, SET NEXT AS PREV
        print(f"Reversed List ---> {str(node)}")
