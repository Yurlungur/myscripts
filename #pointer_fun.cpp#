#include <iostream>
using namespace std;

// find the nth element of an array, the hard way!
int find(int val, int A[]) {
  if (A[0] == val) return val;
  if (A[0] < 0) return -1;
  return find(val,A+1);
}

int main() {
  int A[] = {0,1,2,3,4,5,6,7,-1};

  cout << find(5,A) << endl;

  return 0;
}

