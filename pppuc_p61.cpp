#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
inline void keep_window_open() {char ch; cin>>ch;}

int main()
{
  string previous = " ";
  string current;
  while (cin>>current) {
    if(previous==current)
      cout << "repeated word: " << current << '\n';
    previous = current;
  }
}
