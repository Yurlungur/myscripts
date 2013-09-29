// Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
// Time-stamp: <2013-06-02 18:28:57 (jonah)>

// Include guard
//======================================================================
#ifndef __GAUSSIAN_SYSTEM_H_INCLUDED__
#define __GAUSSIAN_SYSTEM_H_INCLUDED__
//======================================================================


typedef int* IntPtr; // Pointers for ints
typedef double* DoublePtr; // Pointers for doubles
typedef DoublePtr* DoubleArrayPtr; // Pointers for arrays containing doubles

// An NxN matrix. Supports Gaussian elimination operations like row swapping.
class GaussianMatrix {
public:
  // Constructor. Makes an NxN Gaussian Matrix based on matrix m.
  
private:
  int N; // The size of the array
  DoubleArrayPtr m; // NxN array
  IntPtr transposition; // Vector storing row transposition information
  void initialize_transposition(int transposition[N]);
}





//======================================================================
#endif
//======================================================================
  
