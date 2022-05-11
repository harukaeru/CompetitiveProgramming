#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  string S, T;
  int A, B;
  string U;

  cin >> S >> T;
  cin >> A >> B;
  cin >> U;

  map<string, int> counter;
  counter[S] = A;
  counter[T] = B;

  counter[U]--;

  cout << counter[S] << " " << counter[T] << endl;
  return 0;
}
