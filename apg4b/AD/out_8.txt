#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;

  int answer = a < b && a < c ? a : b < a && b < c ? b : c;

  cout << answer << endl;
}
