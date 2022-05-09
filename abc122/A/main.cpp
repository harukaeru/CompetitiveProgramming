#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  char b;
  cin >> b;

  map<char, char> m = {
      {'A', 'T'},
      {'T', 'A'},
      {'C', 'G'},
      {'G', 'C'},
  };

  cout << m[b] << endl;
}
