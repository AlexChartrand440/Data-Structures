"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if value < self.value: # Left
                if self.left is None:
                    self.left = BSTNode(value);
                else:
                    self.left.insert(value);
            elif value >= self.value: # Right
                if self.right is None:
                    self.right = BSTNode(value);
                else:
                    self.right.insert(value);
        else:
            self.value = value;

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target < self.value: # Left
            if self.left is None:
                return False;
            return self.left.contains(target);
        elif target > self.value: # Right
            if self.right is None:
                return False;
            return self.right.contains(target);
        else:
            return True;

    # Return the maximum value found in the tree
    def get_max(self):
        if self.left is None and self.right is None:
            return self.value;
        elif self.right is None:
            val = self.left.get_max();
            if val > self.value:
                return val;
            else:
                return self.value;
        else:
            val = self.right.get_max();
            if val > self.value:
                return val;
            else:
                return self.value;

    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        fn(self.value);

        if self.right is not None:
            self.right.for_each(fn);

        if self.left is not None:
            self.left.for_each(fn);

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        data = [];
        aaa = '';
        if node:
            aaa = self.in_order_print(node.left);
            print(str(node.value));
            aaa = aaa + str(node.value) + '\n';
            aaa = aaa + self.in_order_print(node.right);
            # data = self.in_order_print(node.left);
            # data.append(node.value);
            # data = data + self.in_order_print(node.right);
        print(aaa);
        return aaa;

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
