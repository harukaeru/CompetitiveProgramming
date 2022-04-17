#include <bits/stdc++.h>
using namespace std;

int main() {
  int x = 5;
  cout << x << endl; // 5

  if (x == 5) {
    cout << x << endl; // 5

    string x = "hello"; // int x = 5;のスコープと重なっている
    cout << x << endl; // hello
  }

  cout << x << endl; // 5
}
