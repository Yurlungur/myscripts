//****************************************************************************
// ABOUT THIS PROGRAM (loops.cpp)
//   Written by: Michael Main, August 23, 2004
//   Email address: main@colorado.edu
//   Demonstration program for CSCI 1300
//
// The program demonstrates the use of while-loops and for-loops. 
//**************************************************************************

#include <iostream>   // Provides cin, cout
#include <iomanip>    // Provides setprecision
#include <cstdlib>    // Provides EXIT_SUCCESS
using namespace std;

// Compute how many years are needed to increase savings to a given goal.
// The parameter balance is the initial balance in the account;
// goal is the amount that we want to reach; interest_rate is the
// annual interest rate (such as 0.05 for 5%).
int savings_time(double balance, double goal, double interest_rate);

// Compute how much an account will have after a given number of years
// The parameter balance is the initial balance in the account;
// interest_rate is the annual interest rate (such as 0.05 for 5%);
// years is the number of years that we'll save for. 
double future_balance(double balance, double interest_rate, int years);


int main( )
{
    char response;        // User's response (W or F)
    int many_years;       // Number of years returned by savings_time function
    double final_balance;  // Final balance returned by future_balance function

    // Print the instructions, and get the user's request
    cout << endl;
    cout << "This program illustrates a While loop or a For loop." << endl;
    cout << "Which loop would you like to see? [Please type W or F] ";
    cin >> response;

    // Call a function to illustrate the user's request
    switch (response)
    {
	case 'W': case 'w': // Call savings_time
	    many_years = savings_time(50, 100, 0.10);
	    cout << "Many years to increase $50 to $100 at 10% interest: ";
	    cout << many_years;
	    cout << endl;
	    break;
	case 'F': case 'f': // Call future_balance
	    final_balance = future_balance(50, 0.10, 5);
	    cout << "$50 invested at 10% interest for 5 years increase to: $";
	    cout << setprecision(2) << final_balance;
	    cout << endl;
	    break;
	default:
	    cout << "I'm sorry: " << response << " is not valid." << endl;
    }

    // End the program
    cout << "Please press the return key to end the program." << endl;
    cin.ignore( ); // Read the return key at the end of the user input
    cin.ignore( ); // Read the return key that's pressed to end the program

    return EXIT_SUCCESS;
}


int savings_time(double balance, double goal, double interest_rate)
{
    // Local data...
    int years;            // Number of years that the money is in bank

    years = 0;
    while (balance < goal)
    {
	balance = balance + interest_rate * balance;
	years = years + 1;
    }

    return years;
}


double future_balance(double balance, double interest_rate, int years)
{
    // Local data...
    int i;                 // Loop control variable
    double interest;       // Amount of interest paid in one year

    for (i=0;
	 i<years;
	 i++
        )
    {
	interest = interest_rate * balance;
	balance = balance + interest;
    }

    return balance;
}
