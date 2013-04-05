#!/usr/bin/env python

# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2013-04-05 13:17:37 (jonah)>

# This is a simple program to solve the Fibonacci numbers using
# dynamic programming.

from copy import copy

class Fibonacci:
    """
    A simple class to calculate the Fibonacci numbers using dynamic
    programming. Gets faster with every function call! To find the nth
    Fibonacci number just use

    Fibonacci.nth(n)

    Implemented by using a list of known Fibonacci numbers.

    This class is not meant to be initialized.
    """
    __numbers = [0,1]
    @classmethod
    def nth(self,n):
        "Find the nth Fibonacci number."
        if type(n) != int:
            raise TypeError("The nth Fibonacci number is an integer!")
        if len(self.__numbers) > n:
            return self.__numbers[n]
        out = self.nth(n-1) + self.nth(n-2)
        self.__numbers.append(out)
        return out

    @classmethod
    def set_numbers(self,fib_list):
        """
        If you want to speed up this class by inputting a list of
        known Fibonacci numbers, you can use this method. Simply input
        the list. Only lists are accepted. Only use this method if you
        know the Fibonacci numbers are correct!
        """
        if type(fib_list) != list:
            raise TypeError("The input must be a list!")
        for i in range(len(fib_list)):
            if type(fib_list[i]) != int:
                raise TypeError("The value at index {} is not an integer!".format(i))
        self.numbers = copy(fib_list)
        return

    @classmethod
    def reset_numbers(self):
        """
        Call this command if you messed up the list of Fibonacci numbers.
        It resets the list.
        """
        self.__numbers= [0,1]
        return

    @classmethod
    def output_numbers(self):
        """
        This method outputs a list of all Fibonacci numbers calculated.
        Useful if you want to save the list, or check to see if its correct.
        """
        return copy(self.__numbers)

    @classmethod
    def first_n(self,n):
        "Returns a list of the first n Fibonacci numbers, indexed from 0"
        the_nth = self.nth(n)
        return self.output_numbers()[:n+1]
            
