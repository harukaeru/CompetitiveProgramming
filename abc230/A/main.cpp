#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;

  if (N >= 42) {
    N++;
  }

  cout << "AGC";
  cout << setfill('0') << setw(3) << N;
  cout << endl;

  return 0;
}
