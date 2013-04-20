#!/usr/bin/env python2

# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2013-04-20 16:53:57 (jonah)>

# This program finds the longest increasing subsequence of an input
# sequence (input via command line interaction).

# Input: A list of numbers, no repeats. Any order. Space separated.

# Output: The length of the longest increasing subsequence of the list
# and one such subsequence, space separated.

# This program makes use of my implementation of the binary search
# tree. Make sure it's in the same folder when you call this program!

# ----------------------------------------------------------------------


# Import modules (the binary search tree)
# ----------------------------------------------------------------------
from bst import BinarySearchTree
from copy import copy
# ----------------------------------------------------------------------


# For testing purposes, I have a test input hardcoded.
# ----------------------------------------------------------------------
test_list = [3,9,4,6,1,2,5,8]
# ----------------------------------------------------------------------


# We need to define a new data structure to hold information about our
# subsequences.
class Element:
    """
    The element class is a container class. It holds:
    ----------------------------------------------
    key = An element of the input sequence
    
    length = The length of the longest increasing subsequence of the
             input sequence of which key is the last element.
    
    previous = Points to the previous element in that longest increasing
               subsequence.
    ----------------------------------------------
    """
    def __init__(self,key,length,previous):
        "Constructor"
        self.key = key
        self.length = length
        self.previous = previous

    # Comparison operators
    def __nonzero__(self):
        "Typecast to a boolean"
        return True

    def __lt__(self,other):
        "Returns whether the key is less than other."
        return self.key < other

    def __eq__(self,other):
        "Returns whether the key is equal to other."
        return self.key == other

    def __le__(self,other):
        "Returns whether the key is <= other."
        return self < other or self == other

    def __ne__(self,other):
        "Returns wheter or not self.key == other"
        return not self == other

    def __gt__(self,other):
        "Returns whether or not self.key > other"
        return self.key > other

    def __ge__(self,other):
        "Returns whether or not self.key >= other"
        return self > other or self == other

    def __str__(self):
        "Just typecasts the key to string"
        return str(self.key)

    def __repr__(self):
        outstring = """Element of the sequence:
        key = {}
        length = {}
        previous = {}
        """.format(self.key,self.length,self.previous)
        return outstring

    def __len__(self):
        """
        Returns the length of the longest increasing subsequence that self
        is the final element of.
        """
        return self.length
        
#----------------------------------------------------------------------


# The main algorithm
# ----------------------------------------------------------------------
def build_subsequence_tree(input_list):
    """
    Builds and returns a binary search tree containing elements of the
    sequence using the container class. Also returns the last element
    of a longest increasing subsequence. This way the length of a
    longest increasing subsequence and that sequence can easily be
    calculated.

    input: A list of integers. No repeats!
    output: An ordered pair (bst,longest)
            bst = The binary search tree representing subsequences
            longest = Is the last element of a longest increasing subsequence
                      in its container class.
    """
    # The last element of one of the longest increasing sbusequences
    longest = Element(input_list[0],1,None)
    # The binary search tree we'll use.
    bst = BinarySearchTree()
    # For each element of the input list, we generate an element
    # container class for the element to represent it's behavior as
    # the last element of an increasing subsequence. If this
    # subsequence is longer than any other calculated, we record this.
    for i in input_list:
        greatest_element_less_than_i = bst.find_greatest_key_less_than(i)
        # If it exists, put i in an element that points back to the
        # greatest element less than i. Record that the subsequence is
        # longer.
        if greatest_element_less_than_i != None:
            current = Element(i,
                              greatest_element_less_than_i.length+1,
                              greatest_element_less_than_i)
            bst.insert(current)
            # If this is now the longest increasing subsequence, keep
            # track of that.
            if current.length > longest.length:
                longest = current
        else: # This is the smallest element we've encountered so
              # far. Put it in the BST
            bst.insert(Element(i,1,None))
    return (bst,longest)
                              
def build_output_list(longest_element):
    """
    Builds a list (in order) of a subsequence of the input sequence.
    Takes the longest element output from build_subsequence_tree.
    """
    outlist = [longest_element.key]
    while longest_element.previous != None:
        longest_element = longest_element.previous
        outlist.append(longest_element.key)
    outlist.reverse()
    return outlist

# ----------------------------------------------------------------------


# User interface
# ----------------------------------------------------------------------
def make_output_string(longest_element):
    """
    Given the longest element from build_subsequence_tree,
    produces a string suitable for output.
    """
    # The string for the longest increasing subsequence
    subsequence_string = reduce(lambda x,y: "{} {}".format(x,y),
                                build_output_list(longest_element))
    length_string = str(longest_element.length)
    outstring = "Length: {}\nLongest Increasing Subsequence: {}".format(length_string,subsequence_string)
    return outstring
    
def get_user_input():
    " Requests user input for a list of whole numbers. Parses it into a list."
    raw_data = raw_input("Input the list of whole numbers: ")
    # Cleans it up a little
    data = [int(i) for i in raw_data.lstrip().rstrip().split(' ')]
    return data

# ----------------------------------------------------------------------


# Main loop
# ----------------------------------------------------------------------

def main():
    "Runs when the program is called from the command line."
    input_list = get_user_input()
    subsequence_tree,longest_element = build_subsequence_tree(input_list)
    print make_output_string(longest_element)

if __name__ == "__main__":
    main()

# ----------------------------------------------------------------------
