//****************************************************************************
// ABOUT THIS PROGRAM (heatwave.cxx)
//   Written by: Michael Main, August 24, 2004
//   Email address: main@colorado.edu
//   Exercise for student: Irving Forbush
//
// INPUT: The program prompts the user to enter the height and radius of
//   a tree. To make things simpler, we assume that the tree is a perfect
//   cylinder.  The height is entered first (measured in feet), and then the
//   radius is entered (also measured in feet).
//   The program then prompts the user to enter the number of cubic feet of
//   wood required to heat a house for one day.
//
// OUTPUT: The program calculates the number of days that the tree will heat
//   a house, and outputs this value.
//
// EXAMPLE DIALOG:
//   How tall is your tree in feet?
//   13.2
//   What is the radius of the tree in feet?
//   2.1
//   How many cubic feet of wood will heat a house for a day?
//   40.2
//   That tree will heat a house for 4.54921 days.
//**************************************************************************

#include <iostream>           // Provides cin, cout
#include <cstdlib>            // Provides EXIT_SUCCESS
using namespace std;

const double PI = 3.14159;    // Defined to make the program readable

int main () 
{
    double height;            // Height of a tree in feet
    double radius;            // Radius of a tree in feet
    double requirement;       // Cubic feet of wood to heat house for a day
    double volume;            // Volume of the tree in cubic feet
    double days;              // Number of days that tree will heat house

    // Prompt user for input and read responses
    cout << "How tall is your tree in feet?" << endl;
    cin >> height;
    cout << "What is the radius of the tree in feet?" << endl;
    cin >> radius;
    cout << "How many cubic feet of wood will heat a house for a day?" << endl;
    cin >> requirement;

    // Computations
    volume = height * PI * radius * radius;
    days = volume / requirement;

    // Output days
    cout << "That tree will heat a house for " << days << " days." << endl;

    return EXIT_SUCCESS;
}
