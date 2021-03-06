// Author: Jonah Miller (jonah.maxwell.miller)
// Time-stamp: <2013-06-02 17:36:40 (jonah)>

// This program is a simple implementation of the Gaussian elimination
// algorithm for a simple input matrix, vector equation. For
// simplicity, the equation is input as a global constant.

// The matrix is then printed in the output.


#include <iostream>
#include <cmath>
using namespace std;


// Global constants
// ----------------------------------------------------------------------
const int N = 3; // All matrices are NxN. All vectors are Nx1
// ----------------------------------------------------------------------


// Prototypes
// ----------------------------------------------------------------------
// Prints out the contents of an input vector v of length N. Prints as a
// row vector.
void print_row_vector(double v[N]);

// Prints out the contents of an input vector v of length N. Prints as
// a column vector.
void print_column_vector(double v[N]);

// Prints out the contents of an NxN matrix m
void print_matrix(double m[N][N]);

// Prints out the contents of an input vector v. If the char type is
// 'r', prints a row vector. If type is 'c', prints a column vector.
void print_vector(double v[N], char type);

// Runs a Gaussian elimination algorithm with partial pivoting to
// transform the equation
//                       Ax = b
// with the unkown vector x into the equation
//                       Ux = Mb,
// where U is an upper-triangular matrix. The new equation has the
// same solution vector x as the old equation. Modifies the matrix A
// in-place into U and the vector b in-place into Mb. The third input value
// is a row-transposition vector, described below.
// The row-transposition vector represents swapping to rows (or
// equations) in a matrix equation or system or linear
// equations. This is useful for partial pivoting in Guassian
// elimination without actually swapping two rows of the matrix.  It
// acts as a map from row i to row j of the matrix A. The ith row of
// the transposition vector holds an int, j. i is the index the row
// was initially in. j is the index the row is currently in.
void gaussian_elimination(double A[N][N], double b[N], int transposition[N]);

// Populate a vector as the identity map.
void initialize_transposition(int transposition[N]);

// Given a column j of a matrix A, finds the row i >= j such that
// A_{ij} is the greatest element of column j. Returns i. Uses the
// transposition matrix.
int find_pivot(double A[N][N], int j int transposition[N]);

// ----------------------------------------------------------------------


// Main function
// ----------------------------------------------------------------------
int main() {
  // The equation to solve is:
  // Ax = B
  // here A is a matrix, x is a vector of uknowns, and B is a known vector
  
  double A[N][N] = {{1, 2, 3},  // The NxN matrix to in our system.
		    {4, 5, 6},
		    {7, 8, 9}};
  double b[N] = {10, 11, 12}; // The vector on the rhs of the equation.

  // The transposition map.
  int transposition[N];
  initialize_transposition(transposition);

  // Testing suite
  cout << "The vector b." << endl;
  print_vector(b,'r');
  cout << "The matrix A." << endl;
  print_matrix(A);
  return 0;
}
// ----------------------------------------------------------------------


// Output functions
// ----------------------------------------------------------------------
void print_row_vector(double v[N]) {
  cout << "[";
  for (int i=0; i < N-1; i++) {
    cout << v[i] << ", ";
  }
  cout << v[N-1] << "]" << endl;
}

void print_column_vector(double v[N]) {
  for (int i = 0; i < N; i++) {
    cout << "[" << v[i] << "]" << endl;
  }
}

void print_vector(double v[N], char type) {
  if (type == 'r') {
    print_row_vector(v);
  }
  else if (type == 'c') {
    print_column_vector(v);
  }
  else {
    cout << "ERROR: Type must be either 'r' or 'c'." << endl;
  }
}

void print_matrix(double m[N][N]) {
  for (int i=0; i < N; i++) {
    print_row_vector(m[i]);
  }
}

// ----------------------------------------------------------------------


// Gaussian Elimination Functions
// ----------------------------------------------------------------------

// Make the matrix A upper-triangular and correspond the vector b
// appropriately.
void gaussian_elimination(double A[N][N], double b[N], int transposition[N]) {
  // For every column j of A, find the row i >= j with the largest
  // term A_{ij}. Then swap rows so that i == j and make all A_{ij}
  // zero for i > j.
  for (int j = 0; i < N; i++) {
    
  }
}

void initialize_transposition(int transposition[N]) {
  for (int i = 0; i < N; i++) {
    transposition[i] = i;
  }
}

int find_pivot(double A[N][N], int j, int transposition[N]) {
  double pivot = A[transposition[j]][j]; // The pivot
  int outrow = j; // The row of the pivot
  for (int i = j+1; i < N; i++) {
    if (A[transposition[i]][j] > pivot) {
      pivot = A[transposition[i]][j];
      outrow = i;
    }
  }
  return outrow;
}

// ----------------------------------------------------------------------
