#!/usr/bin/env python

# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2013-04-05 13:43:05 (jonah)>

# This is a simple program to solve the Fibonacci numbers using
# dynamic programming.

from copy import copy
import time

class Fibonacci:
    """
    A simple class to calculate the Fibonacci numbers using dynamic
    programming. Gets faster with every function call! To find the nth
    Fibonacci number just use

    Fibonacci.nth(n)

    Implemented by using a list of known Fibonacci numbers.

    This class is not meant to be initialized.
    """

    # The list of known Fibonacci numbers, indexed from 0.
    # two underscores in front of the name makes the variable private.
    __numbers = [0,1]

    # @classmethod is the same as a static method in java
    # self is the same as this in java.
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
            
def test_driver():
    "This is a test driver for the Fibonacci class."
    print("This is a test driver for the Fibonacci class.")
    print("First let's see how long it takes to calculate the 10th Fibonacci number.")
    x = time.time()
    print("The 10th Fibonacci number is:\n {}".format(Fibonacci.nth(10)))
    print("The operation took {} ms".format(time.time()-x))
    print("Now let's try and calculate the 11th Fibonacci number.")
    x = time.time()
    print("The 11th Fibonacci number is:\n {}".format(Fibonacci.nth(11)))
    print("The operation took {} s".format(time.time()-x))
    print("Faster, right?")
    print("What about the 1000th Fibonacci number?")
    x = time.time()
    print("The 1000th Fibonacci number is:\n {}".format(Fibonacci.nth(1000)))
    print("The operation took {} s".format(time.time()-x))
    print("What about the 1250th number?")
    x = time.time()
    print("The 1250th Fibonacci number is:\n {}".format(Fibonacci.nth(1250)))
    print("The operation took {} s".format(time.time()-x))
    print("What about the 1251st number?")
    x = time.time()
    print("The 1251st Fibonacci number is:\n {}".format(Fibonacci.nth(1251)))
    print("The operation took {} s".format(time.time()-x))
    print("Accessing older values is easy. We can get the first 20 Fibonacci numbers in constant time.")
    x = time.time()
    print("The first 20 Fibonacci numbers are:\n {}".format(Fibonacci.first_n(20)))
    print("The operation took {} s".format(time.time()-x))
    print("Cool, huh?")
    return

# If the program is run from the command line, call the test driver.
if __name__=="__main__":
    test_driver()
