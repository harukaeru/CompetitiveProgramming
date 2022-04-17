#include <bits/stdc++.h>
using namespace std;

int main() {
  // 再帰関数の定義
  function<int(int)> sum = [&](int n) {
    if (n == 0) {
      return 0;
    }
    int s = sum(n - 1);
    return s + n;
  };

  cout << sum(3) << endl;
}
