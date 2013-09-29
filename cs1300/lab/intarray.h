// FILE: intarray.h
// WRITTEN BY: Michael Main(main@colorado.edu), Aug 19, 2004
// PROVIDES: A toolkit of four functions for manipulting integer arrays.
//
// FUNCTIONS in the intarry toolkit:
//   int index_of_minimum(const int array[], int size)
//     Precondition: size must be greater than zero.  It is the number of
//     elements in array (so array goes from [0] to [size-1].
//     Postcondition: The value returned is the index of the smallest entry
//     in array[0] through array[size-1].  If several entries have an equally
//     small value, then the index of the earliest entry is returned.
//   int index_of_maximum(const int array[], int size)
//     Precondition: size must be greater than zero.  It is the number of
//     elements in array (so array goes from [0] to [size-1].
//     Postcondition: The value returned is the index of the largest entry
//     in array[0] through array[size-1].  If several entries have an equally
//     large value, then the index of the earliest entry is returned.
//   void sort(int array[], int size);
//     Precondition: size is the number of elements in array (so array goes
//     from [0] to [size-1].
//     Postcondition: The entries of array have been rearranged so that they
//     are sorted from smallest to largest.
//   void histogram(ostream &out, const int array[], int size);
//     Precondition: size may be from 1 to 70.  It is the number of elements
//     in array (so array goes from [0] to [size-1].  
//     Postcondition: The entries of array have been printed to output stream
//     named out as a histogram, with one column for each element of the array.
//     For example, suppose that size is 11, and the array has these values:
//     array[0]=3, array[1]=2,  array[2]=1, array[3]=0, array[4]=1, array[5]=2,
//     array[6]=0, array[7]=2, array[8]=4, array[9]=6, array[10]=8.  The output
//     from histogram should look something like this:
//       8 |          *
//       7 |          *
//       6 |         **
//       5 |         **
//       4 |        ***
//       3 |*       ***
//       2 |**   * ****
//       1 |*** ** ****
//       0 |+---------+
//     The precise labelling of the axes may be a bit different than this
//     example. 

#ifndef INTARRAY_H
#define INTARRAY_H
#include <iostream>

    int index_of_minimum(const int array[], int size);
    int index_of_maximum(const int array[], int size);
    void sort(int array[], int size);
    void histogram(std::ostream &out, const int array[], int size);

#endif
