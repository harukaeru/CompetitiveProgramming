#include <bits/stdc++.h>
using namespace std;

void f(int &ref) {
  ref = 2;
}

// ポインタを用いた参照渡し
void g(int *ptr) {
  *ptr = 2;
}

int main() {
  int x = 1;
  f(x);  // 参照渡し
  cout << x << endl;

  int y = 1;
  g(&y);  // yのアドレスを渡す
  cout << y << endl;
}
