#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, C, X;
  cin >> A >> B >> C >> X;

  int numbers_of_way_to_pay = 0;

  rep(a, A + 1) {
    rep(b, B + 1) {
      // 500a + 100b + 50c = X
      // 50cはc>=0より0以上にならなければいけない。また、cの最大値はCなので、Cを超えられない
      int candidate_50_coins_value = X - ((500 * a) + (100 * b));
      if (candidate_50_coins_value < 0) {
        continue;
      }

      int candidate_c = candidate_50_coins_value / 50;

      if (candidate_c > C) {
        continue;
      }

      if (candidate_c * 50 == candidate_50_coins_value) {
        numbers_of_way_to_pay++;
      }
    }
  }

  cout << numbers_of_way_to_pay << endl;

  return 0;
}
