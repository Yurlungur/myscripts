#!/usr/bin/env python

"""
simple_iterator.py
Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
Time-stamp: <2014-05-06 12:13:13 (jonah)>

A little timing test to see if C++ or python are comparable for
filling an array.
"""

# Imports
# ----------------------------------------------------------------------
import numpy as np
import time
from numpy.polynomial.hermite import hermval
# ----------------------------------------------------------------------

hermcoeffs = [0]*5 + [1]
N = 1000

def hermite5_v1(x):
    """
    Fifth order hermite polynomial in x. My implementation.
    Pysicist's definition.
    """
    return ((32*x*x - 160)*x*x + 120)*x

def hermite5_v2(x):
    """
    Fifth order hermite polynomial in x. Native implementation.
    Physicist's definition.
    """
    return hermval(x,hermcoeffs)

def combine_v1(i,j):
    "combines i and j. Uses my implementation."
    return hermite5_v1(i+j)

def combine_v2(i,j):
    "combines i and j. Uses native implementation."
    return hermite5_v2(i+j)

def main():
    print "Testing the speed of filling an array."
    print "with the 5th Hermite polynomial."
    print "\t Array is {}x{}.".format(N,N)
    print ""
    print "First we test my implementation."
    start1 = time.time()
    my_array = np.fromfunction(combine_v1,(N,N),dtype=float)
    end1 = time.time()
    diff1 = end1 - start1
    print "The total runtime was:\n\t {} seconds.".format(diff1)
    print ""
    print "Now we test the native implementation."
    start2 = time.time()
    my_array = np.fromfunction(combine_v2,(N,N),dtype=float)
    end2 = time.time()
    diff2 = end2 - start2
    print "The total runtime was:\n\t {} seconds.".format(diff2)
    return

if __name__ == "__main__":
    main()
