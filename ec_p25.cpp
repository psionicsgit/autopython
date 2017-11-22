#include <iostream>
#include <string>
using namespace std;

int main()
{
  string user_name, user_surname;
  cout << "Please enter your first name: ";
  cin >> user_name;
  cout << "And please enter your last name: ";
  cin >> user_surname;
  cout << '\n'
       << "Hello, "
       << user_name
       << " "
       << user_surname
       << " ... and goodbye! \n";

  return 0;
}
