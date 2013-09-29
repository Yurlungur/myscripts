// FILE: sinewave.cxx
// WRITTEN BY: Michael Main(main@colorado.edu), Aug 19, 2004
// A demonstration program showing how the intarray toolkit is used.

#include <iostream>    // Provides cin, cout
#include <cmath>       // Provides sin function
#include <cstdlib>     // Provides EXIT_SUCCESS
#include "intarray.h"  // Provides histogram function
using namespace std;

int main() 
{
    int i;     // for loop control variable
    int a[64]; // Array that contains values of a sin wave

    for (i = 0; i <= 63; i++)
        a[i] = (int) ( (40.0/4.1) * sin(i/10.0) );

    cout << "The function (40/4.1) * sin(x/10), ";
    cout << "for x ranging from 0 to 63:\n\n";
    histogram(cout, a, 64);

    return EXIT_SUCCESS;
}

