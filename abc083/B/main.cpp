#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, A, B;
  cin >> N >> A >> B;

  int t = 0;
  rep(i, N) {
    int j = i + 1;
    int s = 0;
    while (j > 0) {
      s += j % 10;
      j /= 10;
    }

    if (A <= s && s <= B) {
      t += (i + 1);
    }
  }

  cout << t << endl;
  return 0;
}
