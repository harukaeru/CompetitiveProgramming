#include <bits/stdc++.h>
using namespace std;

int main() {

  // 最大値を保持する変数
  int max_num = 0;

  // 今まで受け取った値の中から最も大きな値を返す関数
  auto update_max = [&](int n) {
    if (max_num < n) {
      max_num = n;
    }
    return max_num;
  };

  cout << update_max(5) << endl;
  cout << update_max(2) << endl;
  cout << update_max(10) << endl;
  cout << update_max(4) << endl;
}
