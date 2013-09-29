//****************************************************************************
// ABOUT THIS PROGRAM (bugs.cpp)
//   Written by: Michael Main, Aug 29, 1998
//   Email address: main@colorado.edu
//   Demonstration program for CSCI 1300, lab 2
//
// INPUT: The program prompts the user to enter the length of the base and
//   upright side of a right triangle in inches.
//
// OUTPUT: The program calculates the length of the hypotenuse in inches.
//   It also outputs the equivalent length in feet.
//
// EXAMPLE DIALOG:
//   How tall is your right triangle in inches?
//   3.0
//   What is the base length of the right triangle in inches?
//   4.0
//   That triangle has a hypotenuse of 5.00000 inches.
//   That is th same as 0.416667 feet.
// NOTE: 
//   This version of the program has three bugs in it for the exercise
//   at http://www.cs.colorado.edu/~main/cs1300/cs1300-2.html
//**************************************************************************

#include <iostream>           // Provides cin, cout
#include <cmath>              // Provides sqrt, pow
#include <cstdlib>            // Provides EXIT_SUCCESS
using namespace std;

int main ( )
{
    float height;              // Triangle's height (inches)
    float base;                // Triangle's base (inches)
    float sum_square;          // Sum of squares of height and base
    float hypotenuse;          // Triangle's hypotenuse (inches)
    float feet;                // Triangle's hypotenuse (feet)
    int   zero = 0;            // The number zero, to illustrate an error.

    // Input
    cout << "How tall is your right triangle in inches?" << endl;
    cin  >> height;
    cout << "What is the base length of the right triangle in inches?" << endl;
    cin  >> base

    // Computations
    sum_square = height*height + base*base;
    hypotenuse = 1/zero;
    hypotenuse = sqrt(sum_square);
    feet = (1/12) * hypotenuse;

    // Output answer
    cout << "The hypotenuse is " << hypotenuse << " inches." << endl;
    cout << "This is the same as " << feet << " feet." << endl;

    cout << "Please press the return key to end the program." << endl;
    cin.ignore( ); // Read the return key at the end of the third input
    cin.ignore( ); // Read the return key that's pressed to end the program

    return EXIT_SUCCESS;
}
