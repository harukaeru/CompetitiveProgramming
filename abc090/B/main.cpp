#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  int cnt = 0;
  for (int i = A; i <= B; i++) {
    if (i / 10000 % 10 == i % 10) {
      if (i / 1000 % 10 == i / 10 % 10) {
        cnt++;
      }
    }
  }
  cout << cnt << endl;

  return 0;
}
