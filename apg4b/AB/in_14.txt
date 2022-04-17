#include <bits/stdc++.h>
using namespace std;

struct MyPair {
  int x;
  string y;
  // コンストラクタ
  MyPair() {
    cout << "normal constructor called" << endl;
  }
  // コピーコンストラクタ
  MyPair(const MyPair &old) {
    cout << "copy constructor called" << endl;
    x = old.x + 1;
    y = old.y + " new";
  }
};

int main() {
  MyPair p;  // ここでコンストラクタが呼ばれる
  p.x = 12345;
  p.y = "hello";
  cout << "p.x = " << p.x << endl;
  cout << "p.y = " << p.y << endl;

  MyPair q(p);  // コピーコンストラクタが呼ばれる
  cout << "q.x = " << q.x << endl;
  cout << "q.y = " << q.y << endl;

  MyPair r = q;  // コピーコンストラクタが呼ばれる
  cout << "r.x = " << r.x << endl;
  cout << "r.y = " << r.y << endl;
}
