#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;

  cout << (1000 - (N % 1000)) % 1000 << endl;
  return 0;
}
