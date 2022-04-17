#include <bits/stdc++.h>
using namespace std;

int main() {
  uint32_t *p;

  // uint32_t型の変数の分だけヒープ領域からメモリを確保する
  p = new uint32_t;

  // ポインタを介して使う
  *p = 123;
  cout << *p << endl;

  // メモリを解放する
  delete p;
}
