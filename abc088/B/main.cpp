#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> vec(N);

  rep(i, N) {
    cin >> vec.at(i);
  }

  sort(vec.begin(), vec.end(), greater<int>());

  int a = 0;
  int b = 0;
  rep(i, N) {
    if (i % 2 == 0) {
      a += vec.at(i);
    } else {
      b += vec.at(i);
    }
  }

  cout << a - b << endl;
  return 0;
}
