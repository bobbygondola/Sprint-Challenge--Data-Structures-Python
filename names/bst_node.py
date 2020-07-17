class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    """ PSEUDO FOR INSERT """
    # Insert the given value into the tree
    
    # check if empty
    # if empty, put node at root
    # else if new_node < current.value
    #   left.insert value
    # if >=
    #   right.insert value
    
    
    def insert(self, value):
        new_node = BSTNode(value)
        if value < self.value:              # RECURSION BASE TEST #
            if self.left is None:
                self.left = new_node
            else:                                   # RESTART FUNCTION #
                self.left.insert(value)
        else:                               # OTHER RECURSION TEST # if inserted moved down the list
            if self.right is None:           
                self.right = new_node
            else:
                self.right.insert(value)            # RESTART FUNCTION #
                
                
                
    """ PSEUDO FOR CONTAINS/SEARCH """
    # Return True if the tree contains the value
    # False if it does not
    
    # if node is None:
    #   return False
    # if find.value == node.value
    #   return true
    # else 
    #   if find < node.value   
    #       find on left node
    #   else:
    #       find on right node
    
    def contains(self, target):             # also check for empty DS/array :(
        if self.value == target:            # TEST FOR A FOUND TARGET ON EACH ITERATION #
            return True
        if target < self.value:             # RECURSION BASE TEST # for  lower..
            if self.left:                               # IF EXISTS #
                return self.left.contains(target)           # RECURSIVELY CALL PASSING TARGET #
            else:
                return False
        elif target > self.value:           # RECURSION BASE TEST # for higher..
            if self.right:                                 # IF EXISTS #
                return self.right.contains(target)              # RECURSIVELY CALL PASSING TARGET #
            else:
                return False
                    
            
    """ PSEUDO FOR GET_MAX """
    # Return the maximum value found in the tree
    
    # if theres a right:
    #   get max on right (recursively)
    # else: ..IF NO MORE..
    #   return node.value
    
    def get_max(self):
        
        if self.right:                      # RECURSION TEST
            return self.right.get_max()                 # DIGS DEEPER AND RESETS
        else:                               # NO MORE RIGHTS LEFT..AKA DEEPEST
            return self.value                           # RETURN DEEPEST RIGHT SIDE
        
    
    # # iterative
    # # keep a current largest that weve seen so far.
    # # keep current pointer
    #     current = self
    #     while current.right:
    #         current = current.right
    #     return current.value
    
    
    # iterate down the right child of the current node until no more..(max)
    def get_min(self):
        if self.left:
            return self.left.get_min()
        else:
            return self.value
    

    """ PSEUDO FOR FOR_EACH """
    # Call fn on each self found in the tree
    # Call the function `fn` on the value of each node
    # mimicking for each in JS but in a DataStruc
    # recursively calling fn, through the for_each method
    
    def for_each(self, fn):
        fn(self.value)
        if self.left:                       # RECURSION TEST
            self.left.for_each(fn)                  # RETURN EVERY LEFT INVOKED WITH (FN)
        if self.right:                      # RECURSION TEST
            self.right.for_each(fn)                 # RETURN EVERY RIGHT INVOKED WITH (FN)