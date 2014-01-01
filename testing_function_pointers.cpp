#include <iostream>
#include <vector>
#include <float.h>
#include <cmath>
using std::cout;
using std::endl;
using std::vector;
using std::ostream;
using std::istream;
using std::sqrt;

typedef vector<double> dVector;
typedef dVector::iterator dVIterator;

void f(const vector<double>& b) {
  if (b.size() != 0) {
    cout << "The vector is not empty." << endl;
  }
  else {
    cout << "The vector is empty." << endl;
  }
}

void printdouble(double d) {
  cout << d << endl;
}

void printdouble_ref(double& a) {
  cout << a << endl;
}

void call_func(void (*f)(const vector<double>&)) {
  void (*myf)(const vector<double>&) = f;
  cout << "Calling on a void pointer." << endl;
  vector<double> myvec;
  myf(myvec);
  cout << "Calling on a non-void pointer." << endl;
  myvec.push_back(2.3);
  myf(myvec);
}

void test_vector() {
  vector<double> output(5,5);
  for (dVIterator it = output.begin(); it != output.end(); ++it) {
    cout << *it << ' ';
    cout << endl;
  }
}

dVector vector_factory() {
  dVector output(2,2);
  return output;
}

bool nonzero_vec(const dVector& v) {
  return v.size() > 0;
}

void test_unsigned_ints() {
  unsigned int i = 50;
  cout << "Unsigned: " << i << endl;
  cout << "Signed: " << (int)i << endl;
}

void test_division() {
  double output;
  output = 4
    / 3.0;
  cout << output << endl;
}

void test_do_while() {
  int i = 1;
  while (i != 1 && i < 3) {
    cout << "This is a while loop. Iteration " << i << endl;
    i += 1;
  }
  i = 1;
  do {
    cout << "This is a do while loop. Iteration " << i << endl;
    i += 1;
  } while (i != 1 && i < 3);
}

int main() {
  test_do_while();
  test_unsigned_ints();
  cout << sqrt(DBL_MAX) << "\n" << sqrt(FLT_EPSILON) << endl;
  cout << nonzero_vec(vector_factory()) << endl;
  call_func(f);
  test_vector();
  test_division();
}
