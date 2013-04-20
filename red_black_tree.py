#!/usr/bin/env python2

# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2013-04-20 12:55:40 (jonah)>

# This is an implementation of the red-black tree, an always balanced
# variant of the binary search tree, in python2. My implementation is
# based on the wikipedia article.

# http://en.wikipedia.org/wiki/Red%E2%80%93black_tree

# CURRENTLY, THIS IMPLEMENTATION IS NOT FINISHED!



#----------------------------------------------------------------------

# Global constants
# ----------------------------------------------------------------------

# colors
BLACK = 0 # The black color for the node
RED = 1 # The red colorfor the node

# marks the sentinel node. A single
# sentinel node takes the place of the empty leaf nodes in the
# red-black tree implementation.
SENTINEL = "THIS IS THE SENTINEL RED-BLACK TREE-NODE" 

#----------------------------------------------------------------------

class tree_node:
    """
    A storage class for nodes in the red-black tree.
    Parameters:
    data = the data contained in the node.
    color = the color of the node. Important for the red-black tree.
    parent = the node's parent
    left_child = the left child of the tree
    right_child = the right child of the tree.
    """
    def __init__(self,data,color,parent,
                 left_child,right_child):
        """
        Constructor.
        """
        self.data = data
        self.color = BLACK
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def is_sentinel(self):
        "Returns true if the node is the sentinel. False otherwise."
        return self.data == SENTINEL

    def is_root(self):
        "If the node's parent is None, it's root."
        return self.parent == None

    def __str__(self):
        "String representation."
        return str(self.data)

    def __repr__(self):
        outstring = """Tree node:
        data = {}
        color = {}
        parent = {}
        left_child = {}
        right_child = {}
        """.format(self.data,"red" if self.color==RED else "black",
                   self.parent,self.left_child,self.right_child)
        return outstring


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
        # If this is the sentinel, stop. There is no such node.
        if self.is_sentinel():
            return None
        # If the data is right here. We've found it!
        if self.data == data:
            return self
        if self.data > data:
            return self.left_child.find_child(data)
        else:
            return self.right_child.find_child(data)

    def find_child_with_greatest_key_less_than_data(self,data):
        """
        Finds the child with the greatest key less than the given data.
        """
        target_node = self.find_child(data)
        if target_node == None:
            return None
        if target_node.left_child.is_sentinel():
            return None
        target_node = target_node.left_child
        while not target_node.right_child.is_sentinel():
            target_node = target_node.right_child
        return target_node

    # The following method is for testing purposes
#     @classmethod
#     def make_test_tree(self):
#         # Make nodes
#         G = tree_node("grandparent",BLACK,None,None,None)
#         P = tree_node("parent",BLACK,G,None,None)
#         N = tree_node("node",BLACK,P,None,None)
#         A = tree_node("A",BLACK,P,None,None)
#         B = tree_node("B",BLACK,N,None,None)
#         C = tree_node("C",BLACK,N,None,None)
#         # Connect nodes
#         G.left_child = P
#         P.right_child = N
#         P.left_child = A
#         N.left_child = B
#         N.right_child = C
#         # output
#         return (G,P,N,A,B,C)

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

class red_black_tree:

    """
    The red-black tree data structure.
    """
    def __init__(self):
        """
        Constructor. Initializes an empty red-black tree.
        """
        self.size = 0 # The size of the tree. We keep track of this.
        # The root of the tree. Initially, we don't have one.
        self.root = None 
        # The sentinel node takes the place of all leaves. The parent
        # and child pointers of the sentinel don't matter. They can
        # (and likely will) be safely re-assigned during tree
        # operations.
        self.sentinel = tree_node(SENTINEL,BLACK,None,None,None)

    def size(self):
        "Returns the size of the tree."
        return self.size

    def is_empty(self):
        "Returns true if the tree is empty. False otherwise."
        return self.size() == 0

    # Navigation
    def __find_node(self,data):
        "Finds a node with data if it exists. If it doesn't, return None."
        return self.root.find_child(data)

    def find(self, data):
        "Finds the data if it exists. Otherwise returns 'None.'"
        holder_node = self.__find_node(data)
        if holder_node == None:
            return None
        else:
            return holder_node.data

    # Rotation of tree nodes is important for insertion and deletion
    def __rotate_left(self,node):
        """
        A left rotation demotes a node to the position of its left child
        and promotes the right_child to the position of
        parent. Maintains children in the appropriate place.
        """
        # Rotation is a massively confusing convoluted exercise. I'm just
        # going to use a bunch of pointers to make this easier.
        P = node
        G = node.parent
        N = node.right_child
        A = node.left_child
        B = N.left_child
        C = N.right_child
        # Reassignment
        if G.left_child == P:
            G.left_child = N
        elif G.right_child == P:
            G.right_child = N
        else:
            raise ValueError("The node containing {} has the wrong parent.".format(P))
        N.parent = G
        N.right_child = C
        C.parent = N
        N.left_child = P
        P.parent = N
        P.left_child = A
        A.parent = P
        P.right_child = B
        B.parent = P

    def __rotate_right(self,node):
        """
        A right rotation demotes a node to the position of its right child
        and promotes the left_child to the position of
        parent. Maintains the children in the appropriate places.
        """
        # Rotation is a massively confusing convoluted exercise. I'm just
        # going to use a bunch of pointers to make this easier.
        P = node
        G = P.parent
        C = P.right_child
        N = P.left_child
        A = N.left_child
        B = N.right_child
        # Reassignment
        if G.left_child == P:
            G.left_child = N
        elif G.right_child == P:
            G.right_child = N
        else:
            raise ValueError("The node containing {} has the wrong parent.".format(P))
        N.parent = G
        N.right_child = P
        P.parent = N
        N.left_child = A
        A.parent = N
        P.left_child = B
        B.parent = P
        P.right_child = C
        C.parent = P

    # Adding nodes is complicated. Here are the methods for it.
    def insert(self,data):
        "Inserts a node containing data. Doesn't return anything."
        if self.is_empty():
            inserted_node = self.__insert_root(data)
        else:
            # Insert the node colored red, as you would for a BST.
            inserted_node = self.__insert_child_bst_style(root,data)
            # Now there are a number of cases. We handle them recursively.
        self.__insert_case1(self,inserted_node)
        self.size += 1
    
    def __insert_root(self,root_data):

        """
        Inserts a root node with the input root_data and two sentinel leaves.
        """
        # if a node's parent is none, it's root.
        self.root = tree_node(root_data,BLACK,None,sentinel,sentinel)
        return self.root

    def __insert_child_bst_style(self,node,data):
        """
        Inserts data into the tree as a child of node. This is how data is
        inserted into an ordinary BST. Useful for other inser methods,
        as seen below.

        outputs the inserted node for convenience.
        """
        if data < node.data:
            if node.left_child.is_sentinel():
                node.left_child = tree_node(data,RED,node,sentinel,sentinel)
                outnode = node.left_child
            else:
                outnode = self.left_child.__insert_child_bst_style(node.left_child,data)
        else:
            if node.right_child.is_sentinel():
                node.right_child = tree_node(data,RED,node,sentinel,sentinel)
                outnode = node.right_child
            else:
                outnode = self.right_child.__insert_child_bst_style(node,right_child.data)
        return outnode

    def __insert_case1(self,inserted_node):
        if inserted_node.parent == None:
            inserted_node.color = BLACK
        else:
            self.__insert_case2(self,inserted_node)
        
    def __insert_case2(self,inserted_node):
        """
        Applies if inserted_node's parent is black. In this case, we don't
        need to do anything.
        """
        if (inserted_node.parent.color == BLACK):
            return
        else self.__insert_case3(inserted_node)

    def __insert_case3(self,inserted_node):
        """
        Applies if inserted node's parent and uncle are both red. In this
        case, we repaint both nodes black and we repaint the
        grandparent red.

        Then the grandparent might violate one of our rules. To fix
        this we recursive run the insert cases on the grandparent.
        """
        uncle = inserted_node.uncle()
        if uncle != None and uncle.color == RED:
            inserted_node.parent.color = BLACK
            uncle.color = BLACK
            grandparent = inserted_node.grandparent()
            grandparent.color = RED
            self.__insert_case1(grandparent)
        else:
            self.__insert_case4(inserted_node)

    def __insert_case4(self,inserted_node):
        """
        Applies if the inserted node's parent is red but the uncle is
        black.  Also the current node is the right child of the parent
        is the left child of the grandparent. In this case, we must
        switch the roles of some of the nodes by left tree rotation.

        Swap the words left and right in the above thing to get a
        similar case.

        At this point, some red nodes have red children, but we fix
        this with case 5.
        """
        grandparent = inserted_node.grandparent()
        
        if inserted_node == inserted_node.parent.right_child \
           and inserted_node.parent = grandparent.left_child:
            self.__rotate_left(inseted_node.parent)
            inserted_node = inserted_node.left_child
        elif inserted_node == inserted_node.parent.left_child \
             and inserted_node.parent == grandparent.right_child:
            self.__rotate_right(inserted_node.parent)
            inserted_node = inserted_node.right_child
        else:
            # Do nothing in this case
        self.__insert_case5(inserted_node)
        
    def __insert_case5(self,inserted_node):
        """
        Applies if the inserted node's parent is red but the uncle is black,
        the inserted node is the left child of its parent and the parent is
        the left child of the grandparent.

        In this case, we perform a right-rotation and repaint
        """
        grandparent = inserted_node.grandparent()
        inserted_node.parent.color = BLACK
        grandparent.color = RED
        if inserted_node == inserted_node.parent.left_child:
            rotate_right(grandparent)
        else:
            rotate_left(grandparent)

    # Methods for removal
    def __remove_node_with_two_non_leaf_children(self,node):
        """
        Removes a node if it has two non-leaf children.
        """
        if node.left_child.is_sentinel():
            raise ValueError("This node has at least one leaf child.")
        inorder_predecessor = node.find_child_with_greatest_key_less_than_data(node.data)
        node.data = inorder_predecessor.data
        # We want to remove the inorder predecessor. because it's
        # right child is a leaf, we know it has at least one
        # leaf-child.
        self.__remove_node_with_at_least_one_leaf_child(inorder_predecessor)
        
        

# # For testing purposes:
# # Rotation of tree nodes is important for insertion and deletion
# def rotate_left(node):
#     """
#     A left rotation demotes a node to the position of its left child
#     and promotes the right_child to the position of
#     parent. Maintains children in the appropriate place.
#     """
#     # Rotation is a massively confusing convoluted exercise. I'm just
#     # going to use a bunch of pointers to make this easier.
#     P = node
#     G = node.parent
#     N = node.right_child
#     A = node.left_child
#     B = N.left_child
#     C = N.right_child
#     # Reassignment
#     G.left_child = N
#     N.parent = G
#     N.right_child = C
#     C.parent = N
#     N.left_child = P
#     P.parent = N
#     P.left_child = A
#     A.parent = P
#     P.right_child = B
#     B.parent = P
# 
# def rotate_right(node):
#     """
#     A right rotation demotes a node to the position of its right child
#     and promotes the left_child to the position of
#     parent. Maintains the children in the appropriate places.
#     """
#     # Rotation is a massively confusing convoluted exercise. I'm just
#     # going to use a bunch of pointers to make this easier.
#     P = node
#     G = P.parent
#     C = P.right_child
#     N = P.left_child
#     A = N.left_child
#     B = N.right_child
#     # Reassignment
#     if G.left_child == P:
#         G.left_child = N
#     elif G.right_child == P:
#         G.right_child = N
#     else:
#         raise ValueError("The node containing {} has the wrong parent.".format(P))
#     N.parent = G
#     N.right_child = P
#     P.parent = N
#     N.left_child = A
#     A.parent = N
#     P.left_child = B
#     B.parent = P
#     P.right_child = C
#     C.parent = P
