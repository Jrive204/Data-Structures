class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
		
	# Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        # 
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction 
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)