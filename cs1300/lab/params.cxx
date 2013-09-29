//****************************************************************************
// ABOUT THIS PROGRAM (params.cxx)
//   Written by: Michael Main, August 23, 2004
//   Email address: main@colorado.edu
//   Demonstration program for CSCI 1300
//**************************************************************************

#include <iostream>   // Provides cin, cout
#include <cstdlib>    // Provides EXIT_SUCCESS
using namespace std;

// PROTOTYPES for the functions used...
    
// Function: increment_and_print: ADD ONE TO THE ARGUMENT AND PRINT THE RESULT
void increment_and_print(int i);

int main ()
{
    // Local variable used in the main program:
    int favorite; // User's favorite integer

    // Get the user's favorite integer
    cout << "Please type your favorite integer: " << endl;
    cin >> favorite;

    // Print some output, using the increment_and_print function
    cout << "Yes, " << favorite << " is a fine number." << endl;
    increment_and_print(favorite);
    cout << "I hear that many people like the number ";
    cout << favorite;
    cout << "." << endl;

    // End the program
    cout << "Please press the return key to end the program." << endl;
    cin.ignore( ); // Read the return key at the end of the third input
    cin.ignore( ); // Read the return key that's pressed to end the program

    return EXIT_SUCCESS;
}

void increment_and_print(int i)
{
    i++;
    cout << i << " has always been my personal favorite." << endl;
}
