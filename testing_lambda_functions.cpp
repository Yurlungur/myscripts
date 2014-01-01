#include <iostream>
#include <vector>
using namespace std;

// We use the dVector type a lot, so let's define a type for it
// to make things more readable.
typedef std::vector<double> dVector;

int main()
{
  void (*func)() = [] () { cout << "Hello world" << endl; };
  func(); // now call the function
}
