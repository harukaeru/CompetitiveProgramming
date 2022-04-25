#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, S;
  cin >> N >> S;

  vector<int> A(N), P(N);
  rep(i, N) {
    cin >> A.at(i);
  }
  rep(i, N) {
    cin >> P.at(i);
  }

  vector<int> bucket_A(501, 0);
  vector<int> bucket_P(501, 0);
  rep(i, N) {
    bucket_A.at(A.at(i))++;
    bucket_P.at(P.at(i))++;
  }

  int total_cnt = 0;

  rep(a, bucket_A.size()) {
    int a_cnt = bucket_A.at(a);
    if (a_cnt == 0) {
      continue;
    }
    int expected_p = S - a;
    if (expected_p > 500 || expected_p < 0) {
      continue;
    }
    int p_cnt = bucket_P.at(expected_p);

    total_cnt += (a_cnt * p_cnt);
  }

  cout << total_cnt << endl;

  return 0;
}
