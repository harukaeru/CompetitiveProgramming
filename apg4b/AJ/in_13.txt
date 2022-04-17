#include <bits/stdc++.h>
using namespace std;

int main() {
  uint8_t x = 1;
  uint8_t *p = nullptr;  // 初期値として nullptr を使う
  p = &x;
  *p = 2;
  p = nullptr;  // 使い終わったポインタには nullptr を入れておく
  cout << (int)x << endl;  // 2

  if (p) {
    cout << "not nullptr" << endl;
  } else {
    cout << "nullptr" << endl;
  }
}
