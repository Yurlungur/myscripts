//****************************************************************************
// ABOUT THIS PROGRAM (copyints.cpp)
//   Written by: Michael Main, August 23, 2004
//   Email address: main@colorado.edu
//   Demonstration program for CSCI 1300
//
// The program demonstrates the use of reading and writing from a text
// file. In particular, the program reads integers from numbers.dat
// and writes the same integers to output.dat.
//**************************************************************************

#include <cstdlib>     // Provides EXIT_FAILURE, EXIT_SUCCESS
#include <fstream>     // Provides external file streams
#include <iostream>    // Provides cin, cout, cerr
#include <cctype>      // Provides isspace
using namespace std;

// Function to copy one integer from ins to outs. The output integer
// is written on a single line of output, followed by an endl.
void copy_integer(ifstream& ins, ofstream& outs);

// Function to read and discard any white space from ins. In other
// words, it reads and throws away any spaces, tabs, carraige returns,
// and line feeds. Note that this version will not read an EOF character.
void eatwhite(ifstream& ins);

int main()
{
    // Names for the text files.
    char in_file[40] = "numbers.dat";
    char out_file[40] = "output.dat";

    ifstream ins;            // Input file stream containing bunch of ints
    ofstream outs;           // Output file stream to copy the ints to

    // Open input and output file, exit on any error
    ins.open(in_file);
    if (ins.fail())
    {
        cerr << "***ERROR: Cannot open " << in_file << " for input." << endl;
	return EXIT_FAILURE;
    }
    outs.open(out_file);
    if (outs.fail())
    {
	cerr << "***ERROR: Cannot open " << out_file << " for output." << endl;
        return EXIT_FAILURE;
    }

    // Copy each integer from input file to output file. Notice that the loop
    // continues as long as the input stream has not encountered any bad input
    // (ins is still true) and the next character is not EOF.
    eatwhite(ins);
    while (ins && (ins.peek( ) != EOF))
    {
	copy_integer(ins, outs);
	eatwhite(ins);
    }   

    // Display a message on the screen and end the program
    cout << "Input file " << in_file << " copied to file " << out_file << endl;
    ins.close();
    outs.close();
    return EXIT_SUCCESS;
}


void copy_integer(ifstream& ins, ofstream& outs)
{
    int next_integer;    // integer read from ins and written to outs

    ins >> next_integer;
    outs << next_integer << endl;
}


void eatwhite(ifstream& ins)
{
    while (ins && isspace(ins.peek()))
        ins.ignore();
}

