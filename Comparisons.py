#!/usr/bin/env python2

# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2013-05-06 16:18:39 (jonah)>

# This implements a class that counts the number of comparisons
# made. Dead simple implementation.

# ----------------------------------------------------------------------

# Import modules
import operator # The greater than, less than, etc.

class Comparisons:
    def __init__(self):
        "Initializes a comparisons class instance."
        self.__count = 0

    def count(self):
        "Returns the current count."
        return self.__count
        
    def reset_count(self):
        "Resets the count variable."
        self.__count = 0

    def compare(self,a,b,comparison_operator):
        "Compares a and b using the comparison operator."
        self.__count += 1
        return comparison_operator(a,b)

    def lt(self,a,b):
        "Returns a < b"
        return self.compare(a,b,operator.lt)

    def gt(self,a,b):
        "returns a > b"
        return self.compare(a,b,operator.gt)

    def le(self,a,b):
        "returns a <= b"
        return self.compare(a,b,operator.le)

    def ge(self,a,b):
        "returns a >= b"
        return self.compare(a,b,operator.ge)

    def eq(self,a,b):
        "returns a == b"
        return self.compare(a,b,operator.eq)

    def ne(self,a,b):
        "returns a != b"
        return self.compare(a,b,operagor.ne)
