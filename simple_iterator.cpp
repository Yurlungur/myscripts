// simple_iterator.cpp

// Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
// Time-stamp: <2014-05-06 14:05:12 (jonah)>

// A little timing test to see if C++ or python are comparable for
// filling an array.

// ----------------------------------------------------------------------

// Include
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

// Important constants
const int N = 1000; // 1000x1000 matrix => 8 GB of memory
                    // Asking for more memory => segfault

// Prototypes
// ----------------------------------------------------------------------
// The fifth Hermite polynomial in x.
double hermite5(double x);

// Combines two integers i and j into a single double somehow.
double combine(int i, int j);
// ----------------------------------------------------------------------



// main function
// ----------------------------------------------------------------------
int main() {
  cout << "got to main" << endl;
   clock_t t1,t2; // initial and final cpu times
   cout << "defined clock times" << endl;
   float diff; // The difference in cpu cycles
   float seconds; // The difference in times in seconds
   double testA [N][N]; // Test array

   cout << "Testing the speed of filling an arryay\n"
        << "with the 5th Hermite polynomial.\n"
        << "\t Array is " << N << "x" << N << ".\n"
        << endl;
   t1 = clock();
   
   // The loop
   for (int i = 0; i < N; i++) {
     for (int j = 0; j < N; j++) {
       testA[i][j] = combine(i,j);
     }
   }
   
   t2 = clock();
   diff = (float(t2) - float(t1));
   seconds = diff / CLOCKS_PER_SEC;
   
  cout << "The total runtime was:\n"
       << "\t " << seconds << " seconds."
       << endl;
  
  return 0;
}
// ----------------------------------------------------------------------


// Implementations
// ----------------------------------------------------------------------
double hermite5(double x) {
  return ((32*x*x - 160)*x*x + 120)*x;
}
double combine(int i, int j) {
  return hermite5(i + j);
}
// ----------------------------------------------------------------------

