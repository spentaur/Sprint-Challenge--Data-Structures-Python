class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value < value:
            # if the value we are trying to insert is greater than the current
            # node value, add it to the right
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        else:
            # if it is less than, add it to the left
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif (target < self.value) and self.left:
            # if the target is less than the current value, check on the left
            return self.left.contains(target)
        elif (target > self.value) and self.right:
            # if the target is greater than the current value, check the right
            return self.right.contains(target)
        else:
            # not in here
            return False
