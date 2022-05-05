#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

int main() {
  int N, K;
  cin >> N >> K;

  vector<int> vec(N);
  rep(i, N) {
    cin >> vec.at(i);
  }

  for (int i = 0; i < (1 << N); i++) {
    bitset<20> b(i);
    int sum = 0;
    for (int j = 0; j < N; j++) {
      int b_flag = b.test(j);
      int v = vec.at(j);
      sum += b_flag * v;
    }

    if (sum == K) {
      cout << "YES" << endl;
      return 0;
    }
  }

  cout << "NO" << endl;
}