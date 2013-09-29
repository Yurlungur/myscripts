// CSCI 1300 - Student Name: ...
// LAB EXAM
// This file provides a small main program to help you test your solution
// for the quiz_average function. You must implement this function at
// the bottom of this file.

#include <iostream>
#include <cstdlib>
using namespace std;

const int SIZE = 11;

double quiz_average(int s[11]);
void get_array(const char message[], int s[], int n);

int main( )
{
    int sample_s[SIZE];

    for (;;)
    {	// This loop repeats until user presses CTRL-C
	cout << "---------------------------------------------------" << endl;
	cout << "Enter CTRL-C to quit." << endl;
	get_array("s", sample_s, SIZE);
	cout << "The function returned: " << quiz_average(sample_s) << endl;
    }

    return EXIT_SUCCESS;
}

void get_array(const char message[], int s[], int n)
{
    int i;
    
    cout << "Please enter the values of the array " << message << ":" << endl;
    for (i = 0; i < n; i++)
    {
	cout << "  " << message << "[" << i << "]: ";
	cin >> s[i];
    }
}


// The array s contains 11 non-negative integers. At least one
// of the entries in s will be non-zero.
// The function interprets the values in s as frequency counts for the quiz
// scores in a class. For example, if s[9] is 42, then this means that 42
// students in the class received the score of 9 on the quiz.
// The return value of the function is the average quiz score for the 
// entire class.
// EXAMPLES:
// Suppose s is {1, 2, 4, 2, 4, 2, 4, 1, 0, 1, 2}. This means that:
// 1 student scored 0 on the quiz,
// 2 students scored 1 on the quiz,
// 4 students scored 2 on the quiz,
// 2 students scored 3 on the quiz, ... and so on.
// In all, 23 students took the quiz and the overall average is:
// (1*0 + 2*1 + 4*2 + 2*3 + 4*4 + 2*5 + 4*6 + 1*7 + 0*8 + 1*9 + 2*10)/23
// which is about 4.435.
double quiz_average(int s[11])
{
    // STUDENT MUST IMPLEMENT THIS FUNCTION
}
