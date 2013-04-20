#!/usr/bin/env python2

# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2013-04-20 15:02:14 (jonah)>

# This is an implementation of a simple binary search tree in python.

class tree_node:
    """
    A storage class for nodes in the binary search tree
    Parameters:
    data = the data contained in the node.
    parent = the node's parent
    left_child = the left child of the tree
    right_child = the right child of the tree.
    """
    def __init__(self,data,parent,
                 left_child,right_child):
        """
        Constructor.
        """
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def is___root(self):
        "If the node's parent is None, it's __root."
        return self.parent == None

    # Some internal tree navigation methods. May raise errors if the
    # node is not in a tree.
    def sibling(self):
        "Returns self's parent's other child."
        if self.parent == None: # no parent means no sibling.
            return None
        if self == self.parent.left_child:
            return self.parent.right_child
        if self == self.parent.right_child:
            return self.parent.left_child
        # something went wrong
        raise ValueError("Parent-child mismatch! Node: {}".format(self))

    def grandparent(self):
        "Returns self's parent's parent."
        if self.parent == None: # No parent means no grandparent
            return None
        return self.parent.parent

    def uncle(self):
        "Returns self's parent's sibling."
        grandparent = self.grandparent()
        if grandparent == None:
            return None # No grandparent means no uncle
        if self.parent == grandparent.right_child:
            return grandparent.left_child
        else:
            return grandparent.right_child

    def find_child(self,data):
        """
        Returns the node with the appropriate data, if it
        exists. otherwise returns None.
        """
        if data == None:
            raise ValueError("You must input some data to find.")
        # If the data is right here. We've found it!
        if self.data == data:
            return self
        if self.data > data:
            if self.left_child == None: # no such data exists.
                return None
            else:
                return self.left_child.find_child(data)
        else:
            if self.right_child == None: # no such data exists.
                return None
            else:
                return self.right_child.find_child(data)

    def find_smallest_child(self):
        "Returns smallest child of self. May return self."
        current_node = self
        while current_node.left_child != None:
            current_node = current_node.left_child
        return current_node

    def find_greatest_child(self):
        "Returns the greatest child of self. May return self."
        current_node = self
        while current_node.right_child != None:
            current_node = current_node.right_child
        return current_node

    def find_child_with_greatest_key_less_than_data(self,data):
        """
        Finds the child with the greatest key less than the given data.
        """
        current_node = self.find_child(data)
        if current_node == None or current_node.left_child == None:
            return None
        current_node = current_node.left_child
        return current_node.find_greatest_child()

    def inorder_traversal_of_subtree(self,command):
        """
        Using inorder tree traversal, calls command on every node in the
        subtree with self as __root.

        Command is a function.
        """
        if self.left_child != None:
            self.left_child.inorder_traversal_of_subtree(command)
        command(self)
        if self.right_child != None:
            self.right_child.inorder_traversal_of_subtree(command)

    def insert_node_in_subtree(self,data):
        "Inserts a node with the appropriate datain the BST subtree of self."
        if data < self.data:
            if self.left_child == None:
                self.left_child = tree_node(data,self,None,None)
            else:
                self.left_child.insert_node_in_subtree(data)
        else:
            if self.right_child == None:
                self.right_child = tree_node(data,self,None,None)
            else:
                self.right_child.insert_node_in_subtree(data)

    def pop(self):
        """
        The node deletes itself from the tree.

        Doesn't work if the tree is __root.

        Only use this if the node has two leaves! Otherwise you could
        destroy a subtree!
        """
        if self.is___root():
            raise ValueError("This node is the __root!")
        if self == self.parent.left_child:
            self.parent.left_child = None
        elif self == self.parent.right_child:
            self.parent.right_child = None
        else:
            raise ValueError("Parent-child mismatch for {}".format(self))
        return self.data
        
    # Comparisons
    def __lt__(self,other):
        return self.data < other

    def __eq__(self,other):
        return self.data == other

    def __le__(self,other):
        return self.__lt__(other) or self.__eq__(other)

    def __ne__(self,other):
        return not self.__eq__(other)

    def __gt__(self,other):
        return not self.__le__(other)

    def __ge__(self,other):
        return not self.__lt__(other)

    def __nonzero__(self):
        return True

    def __len__(self):
        return len(self.data)

    def __str__(self):
        "String representation."
        return str(self.data)

    def __repr__(self):
        outstring = """Tree node:
        data = {}
        parent = {}
        left_child = {}
        right_child = {}
        """.format(self.data,self.parent,self.left_child,self.right_child)
        return outstring

class binary_search_tree:
    """
    A binary search tree data structure. Can only be initialized empty.
    """
    def __init__(self):
        "Constructor. Initializes an empty BST."
        self.__size = 0 # The __size of the tree. We keep track of this.
        # The __root of the tree. Initially we don't have one.
        self.__root = None

    def is_empty(self):
        "Returns true if the tree is empty. False otherwise."
        return self.__size == 0

    # Navigation
    def __find_node(self,data):
        "Find a node with data if it exists. If it doesn't, return None."
        if self.__root == None:
            return None
        return self.__root.find_child(data)

    def find(self,data):
        "Finds the data if it exists. Otherwise returns 'None.'"
        holder_node = self.__find_node(data)
        if holder_node == None:
            return None
        return holder_node.data

    def find_greatest_key_less_than(self,data):
        """
        Find the greatest key less than data, if it exists.
        Otherwise return None.
        """
        if self.is_empty():
            return None
        node = self.__root.find_child_with_greatest_key_less_than_data(data)
        if node == None:
            return None
        return node.data

    def find_max(self):
        "Finds the max data in the tree. If tree is empty, returns None."
        if self.is_empty():
            return None
        return self.__root.find_greatest_child().data

    def find_min(self):
        "Finds the min data in the tree. If tree is empty, returns None."
        if self.is_empty():
            return None
        return self.__root.find_smallest_child().data

    def inorder_traversal(self,command):
        """
        Applies command to every element of the tree in order.
        If the tree is empty, does nothing.
        """
        if self.is_empty():
            return
        self.__root.inorder_traversal_of_subtree(command)

    # A utility tool
    def __swap_node_data(self,node1,node2):
        "Swaps the data in node1 and node2"
        tempdata = node1.data
        node1.data = node2.data
        node2.data = tempdata

    # Insertion
    def insert(self,data):
        "Inserts a node containing data. Doesn't return anything."
        if self.is_empty():
            self.__insert___root(data)
        else:
            self.__root.insert_node_in_subtree(data)
        self.__size += 1

    def __insert___root(self,data):
        "Inserts a __root node with the input data, no parent, and no children."
        self.__root = tree_node(data,None,None,None)
        
    # Removal
    # Removal methods return the data too. Just in case you want it.
    def __remove_node(self,node):
        "Removes the input node and maintains tree invariants."
        outdata = node.data # The data of the node to remove. We'll
                            # return it.
        
        # We break up into a number of cases
        if self.__size == 1:
            # Then the node to remove is __root. Tree invariant will be
            # maintained if we just delete.
            self.__root = None
        elif node.left_child == None and node.right_child == None:
            # In this case, we have a leaf node and we can just get rid of it
            node.pop()
        elif node.left_child == None or node.right_child == None:
            # The node only has one child. We can safely replace it
            # with that child.
            if node.left_child == None: # Find the child
                child = node.right_child
            else:
                child = node.left_child
            # Replace the node with the child
            if node == node.parent.left_child:
                node.parent.left_child = child
            elif node == node.parent.right_child:
                node.parent.right_child = child
            else:
                raise ValueError("Parent-child mismatch for {}!".format(node))
        else: # The node has two non-leaf children.
            # In this case, we
            # swap the node with its inorder precessor, which can be
            # safely removed using one of the other cases.
            to_replace = node.find_child_with_greatest_key_less_than_data(node.data)
            # The nodes are swapped
            self.__swap_node_data(node,to_replace)
            # We delete the to_replace node.
            self.__remove_node(to_replace)
            # The __size was reduced in the recursive call, so we don't
            # want to reduce it again.
            return outdata

        # Shrink the tree and return outdata
        self.__size -= 1
        return outdata

    def remove(self,data):
        """"
        Removes an node containing data. Returns the data. If no such
        node exists, returns None.
        """
        to_remove = self.__find_node(data)
        if to_remove == None:
            return None
        else:
            return self.__remove_node(to_remove)

    # Typical utility commands
    def __len__(self):
        "Length of the tree."
        return self.__size

    def __nonzero__(self):
        "Boolean typecasting"
        return bool(len(self))

    def __str__(self):
        "Returns the string for the tree."
        outlist = []
        append_command = lambda x: outlist.append(str(x))
        self.inorder_traversal(append_command)
        return "[" + reduce(lambda x,y: "{}, {}".format(x,y),outlist) + "]"

    def __repr__(self):
        outstring = """Binary search tree:
        size = {}
        elements = {}
        """.format(len(self),str(self))
        return outstring
        
