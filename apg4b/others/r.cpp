#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

int main() {
  int N;
  cin >> N;

  int cnt = 0;
  while (N > 1) {
    if (N % 2 == 0) {
      cnt++;
      N = N / 2;
      continue;
    }
    break;
  }

  cout << cnt << endl;
}