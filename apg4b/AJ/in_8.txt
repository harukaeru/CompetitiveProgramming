#include <bits/stdc++.h>
using namespace std;

int main() {
  int x = 123;

  int *p = &x;  // xを指すポインタ
  int *q = &x;  // yを指すポインタ

  // アドレスの比較
  if (p == q) {
    cout << "p == q" << endl;
  } else {
    cout << "p != q" << endl;
  }
}
