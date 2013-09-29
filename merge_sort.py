#!/usr/bin/env python2

# merge_sort.py

# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2013-05-06 17:52:52 (jonah)>

# A dead simple implementation of merge sort. Includes testing suite
# tools.

# WARNING: VERY VERY SLOW. USES CODING TRICKS TO MAKE EASY, BUT SLOW CODE

# ----------------------------------------------------------------------

# Import modules
import sys # for command line interface
import operator
import Comparisons
from random import shuffle # For the test suite

# Mergesort methods

# ----------------------------------------------------------------------

def merge(list1, list2,comparison_class):
    """
    Takes the lists list1 and list2 and merges them into a single list.
    Assumes list1 and list2 are sorted. If they are sorted, the output
    list will be sorted. If they are not, the output is unclear.

    comparison_class passes a class containing the operators such as
    greater-than, less-than, etcetera. Part of the testing suite tools.
    """
    # The output list
    output = []

    # While at least one list has nonzero length, loop through the
    # following checks
    while len(list1) > 0 or len(list2) > 0:
        # If both lists are nonzero, take the min(list1[0],list2[0])
        if len(list1) > 0 and len(list2) > 0:
            if comparison_class.le(list1[0],list2[0]):
                output.append(list1[0])
                # Reassign the first list to its sublist starting at
                # index 1
                list1 = list1[1:]
            else:
                output.append(list2[0])
                # Reassign the second list to its sublist starting at
                # index 1
                list2 = list2[1:]
        elif len(list1) > 0: # list2 is empty.
            output += list1 # Just append list1 to the output.
            list1 = [] # Make sure list1 is empty
        else: # list1 is empty but list2 is not.
            output += list2 # Just append list2 to the output.
            list2 = [] # Make sure list2 is empty

    # We're done! Return the output.
    return output

def merge_sort(list_to_sort,comparison_class = operator):
    """
    Sorts the input list by merge sort. Usually uses the operator
    comparisons. But this can be overridden. Returns a sorted list on
    output.
    """
    # If the list size is zero or one, consider it sorted and return it.
    if comparison_class.le(len(list_to_sort),1):
        return list_to_sort
    # Otherwise, split the list into two sublists, sort each one
    # recursively, and merge them.
    pivot = len(list_to_sort)/2 # The midpoint of the lists.
    left_hand_list = list_to_sort[:pivot]
    right_hand_list = list_to_sort[pivot:]
    # Sort the two lists recursively
    left_hand_list = merge_sort(left_hand_list,comparison_class)
    right_hand_list = merge_sort(right_hand_list,comparison_class)
    # Merge the two lists and exit
    output = merge(left_hand_list,right_hand_list,comparison_class)
    return output

# Test suite

# ----------------------------------------------------------------------
def count_comparisons(list_to_sort):
    """
    Counts the number of comparisons required to sort the input list.
    """
    # Initialize the comparisons class
    comp = Comparisons.Comparisons()
    # Sort the list using the comparisons class
    output_list = merge_sort(list_to_sort,comp)
    # Return an ordered pair. First element is the number of
    # comparisons. Second element is the sorted list.
    return (comp.count(),output_list)

def make_random_list(n):
    "Makes a random list of length n."
    outlist = [i for i in range(n)]
    shuffle(outlist)
    return outlist

def average_comparisons(n,trials = False):
    """
    Calculates empirically the number of comparisons required to sort
    a list of length n. Uses trials trials. If trials=False, calculates
    trials as min(100,n).
    """
    if trials == False:
        trials = min(100,n)
    counts =[count_comparisons(make_random_list(n))[0] for i in range(trials)]
    return sum(counts)/len(counts)

if __name__ == "__main__":
    print average_comparisons(int(sys.argv[1]))
