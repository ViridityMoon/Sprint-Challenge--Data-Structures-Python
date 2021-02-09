import time

start_time = time.time()

f = open('./names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('./names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
"""
   Encapsulation of (BinarySearchTreeNode) 'BSTNode'; takes in a value
   that it captures and saves as 'value'.
"""
class BSTNode:
    """
        __init__() Method; takes in a value and captures it as 'value'.
        Initializes 'left' node and 'right' node values to 'None'. These
        will be full BSTNode class Objects later.
    """
    def __init__(self, value):
        # value held by the BSTNode
        self.value = value
        # value to the left of the BSTNode, a full BSTNode Object
        # initializes to None
        self.left = None
        # value to the right of the BSTNode, a full BSTNode Object
        # initializes to None
        self.right = None

    """
        insert() Method; takes in a value and inserts it into the 'Tree'.
        BinarySearchTree's do not allow duplicate numbers, so we run the contains()
        method to see if it would be a duplicate
        It will follow a trend of:
        smaller numbers to the left of any specific node,
        bigger numbers to the right of any specific node.
    """
    def insert(self, value):
        # We need to run the contains() method to see if the value is already within
        # the tree, which is not allowed
        if not self.contains(value):
            # check if inserted value is less than the head's value
            if value < self.value:
                # check if there is already a BSTNode to the left
                if not self.left:
                    # create a new BSTNode with the value
                    new_node = BSTNode(value)
                    # insert that value into the new BSTNode
                    self.left = new_node
                # otherwise
                else:
                    # Recursively invoke the left BSTNode's insert method, 
                    # beginning the process again but to the left. The 
                    # value can't occupy a node that already has a value.
                    self.left.insert(value)
            # if the value is greater than or equal to the head's value
            else:
                # check if there is already a BSTNode to the right
                if not self.right:
                    # create a new BSTNode with the value
                    new_node = BSTNode(value)
                    # insert that value into the right node
                    self.right = new_node
                # otherwise
                else:
                    # Recursively invoke the right BSTNode's insert method, 
                    # beginning the process again but to the right. The 
                    # value can't occupy a node that already has a value.
                    self.right.insert(value)
        else:
            return value


    """
        contains() Method; will determine if a full 'BinarySearchTree' contains
        the provided 'target'. It will run and then recursively run again to 
        check all of the values to see if the 'Tree' has it anywhere within it
        or it's left or right BSTNodes.
    """
    def contains(self, target):
        # if the head is the entered target; the 'Tree' does in fact contain the target
        if self.value == target:
            # so return True
            return True
        
        # if the target is less than the value of the BSTNode, then we know to proceed
        # to the left, as in a 'BinarySearchTree', all values to the left of any given
        # BSTNode would be smaller.
        if target < self.value:
            # if there is no value to the left; then we have reached the end of our search
            # this would imply the value entered is lower than any value in the 'Tree'
            if not self.left:
                # the target is not contained in the 'Tree'
                return False
            # otherwise
            else:
                # if there is a value within the left node already, we will recursively
                # invoke the contains method on the left BSTNode, if the value is within
                # that BSTNode, then it will immediately return True, otherwise it will
                # search again
                return self.left.contains(target)
        # if the target is greater than the value of the BSTNode, then we know to proceed
        # to the right, as in a 'BinarySearchTree', all values to the right of any given
        # BSTNode would be greater.
        else:
            # # if there is no value to the right; then we have reached the end of our search
            # this would imply the value entered is greater than any value in the 'Tree'
            if not self.right:
                # the target is not contained in the 'Tree'
                return False
            # otherwise
            else:
                # if there is a value within the right node already, we will recursively
                # invoke the contains method on the right BSTNode, if the value is within
                # that BSTNode, then it will immediately return True, otherwise it will
                # search again
                return self.right.contains(target)



# Initial thoughts: add all the values of 'names_1' into a BST, then loop
# through, run the contains function on 'names_2', if true, append them
# to duplicates
"""
Finds which values are equal in 'names_1' and 'names_2' and appends them to an array; then returns that array.
"""
def duplicates():
    # Make an array to append the values to
    duplicates = []  # Return the list of duplicates in this data structure
    # create a new 'BinarySearchTree'
    bst = BSTNode("Names - Head")
    # Loop through and grab all the values in 'names_1'
    for name_1 in names_1:
        # Insert those into the 'Tree'
        bst.insert(name_1)
    
    # Loop through for each value in 'names_2'
    for name_2 in names_2:
        # run the bst's contains() method on each value in name_2
        if bst.contains(name_2):
            # any values that are contained are the same, append them to duplicates
            duplicates.append(name_2)
    # return the array
    return duplicates


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates())} duplicates:\n\n{', '.join(duplicates())}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
