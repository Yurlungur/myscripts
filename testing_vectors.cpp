#include <iostream>
#include <vector>
using namespace std;

// We use the dVector type a lot, so let's define a type for it
// to make things more readable.
typedef std::vector<double> dVector;

int main()
{
  dVector testing(3,0);
  cout << "size = " << (int)testing.size() << endl;
  cout << "for i from 0 to 3 exclusive." << endl;
  for (int i = 0; i < (int)testing.size(); i++) {
    cout << testing[i] << endl;
  }
  cout << "iterator" << endl;
  for (dVector::const_iterator it = testing.begin();
       it != testing.end(); ++it) {
    cout << (*it) << endl;
  }

  return 0;
}
