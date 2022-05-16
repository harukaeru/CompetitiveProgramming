#include <bits/stdc++.h>
#include <math.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> vec(N);
  rep(i, N) {
    cin >> vec.at(i);
  }

  int cnt = 0;
  while (cnt < 100) {
    rep(i, N) {
      int k = vec.at(i);
      if (k % 2 == 1) {
        cout << cnt << endl;
        return 0;
      }
      vec.at(i) = k / 2;
    }
    cnt++;
  }

  return 0;
}
