// CSCI 1300 - Student Name: ...
// LAB EXAM
// This file provides a small main program to help you test your solution
// for the dot function. You must implement this function at
// the bottom of this file.

#include <iostream>
#include <cstdlib>
using namespace std;

const int MAX = 100;

double dot(double s[], double t[], int n);
void get_array(const char message[], double s[], int n);

int main( )
{
    double sample_s[MAX];
    double sample_t[MAX];
    int size;

    for (;;)
    {	// This loop repeats until user presses CTRL-C
	cout << "---------------------------------------------------" << endl;
	cout << "Enter CTRL-C to quit, or ";
	cout << "enter the value of size (up to " << MAX << "): ";
	cin >> size;
	get_array("s", sample_s, size);
	get_array("t", sample_t, size);
	cout << "The dot product is: " << dot(sample_s, sample_t, size) << endl;
    }

    return EXIT_SUCCESS;
}

void get_array(const char message[], double s[], int n)
{
    int i;
    
    cout << "Please enter the values of the array " << message << ":" << endl;
    for (i = 0; i < n; i++)
    {
	cout << "  " << message << "[" << i << "]: ";
	cin >> s[i];
    }
}


// Both arrays s and t contains at least n double numbers (and n >= 0). 
// The return value of the dot function is the "dot product" defined by
// s[0]*t[0] + s[1]*t[1] + s[2]*t[2] + ... s[n-1]*t[n-1].
// EXAMPLE: Suppose that s contains { 1.1, 2.1, 3.1}.
// and suppose that t contains      { 1.4, 2.0, 3.0}.
// Then: dot(s, t, 3) is 1.1*1.4 + 2.1*2.0 + 3.1*3.0 
// Note: dot(s, t, 0) is always zero.
double dot(double s[], double t[], int n)
{
    // STUDENT MUST IMPLEMENT THIS FUNCTION
}
