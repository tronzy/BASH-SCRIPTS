// Author: Michael Lawal Okenwa DUO670

#include <iostream>

using namespace std;

int main() {
   float num1;
   int num2;

   // Accept two numbers using input stream
   cout << "Enter a float number: ";
   cin >> num1;
   cout << "Enter an integer number: ";
   cin >> num2;

   // Add two numbers using arithmetic operators
   int sum_int = static_cast<int>(num1) + num2;  // Cast float to int for integer sum
   float sum_float = num1 + num2;  // Direct addition for float sum

   // Display the numbers in integer and float form using output stream
   cout << "Sum of two numbers in integer form: " << sum_int << endl;
   cout << "Sum of two numbers in float form: " << sum_float << endl;

   return 0;
}
