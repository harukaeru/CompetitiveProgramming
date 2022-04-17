#include <bits/stdc++.h>
using namespace std;

void test() {

  // test関数のスコープで変数numを宣言
  int num = 5;
  cout << num << endl; // 5

  return;
}

int main() {
  // main関数のスコープで変数numを宣言
  int num = 10; 
  test();
  cout << num << endl; // 10
}
