#include <bits/stdc++.h>
using namespace std;

int main() {
  // int型1つ分の領域を確保(123で初期化)
  unique_ptr<int> p1 = make_unique<int>(123);
  *p1 += 1;
  cout << *p1 << endl;

  unique_ptr<int> p2;
  p2 = move(p1); // メモリの所有権をp2に移動
  //*p1 += 10;  // p1は所有権を失ったのでエラー
  *p2 += 1;
  cout << *p2 << endl;
}  // ここでp2の持っていた所有権が無効になり自動的にメモリが回収される
