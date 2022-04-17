#include <bits/stdc++.h>
using namespace std;

struct MyPair {
  int x;
  string y;
  // 代入演算子をオーバーロード
  void operator=(const MyPair &other) {
    cout << "= operator called" << endl;
    x = other.x;
    y = other.y;
  }
};

int main() {
  MyPair a = {123, "hello"};

  MyPair b;
  b = a;  // 代入演算子が呼ばれる

  cout << "b.x = " << b.x << endl;
  cout << "b.y = " << b.y << endl;
}
