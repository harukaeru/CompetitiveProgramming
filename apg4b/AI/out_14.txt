#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> a = {1, 2, 3, 5};
  // 3の要素を指すイテレータ
  auto itr = find(a.begin(), a.end(), 3);

  // もし存在しなければ、a.end()が返る
  if (itr == a.end()) {
    cout << "not found" << endl;
  } else {
    // itrが添字の何番目を指すかを求める
    int idx = distance(a.begin(), itr);
    cout << "a[" << idx << "] = " << *itr << endl;
  }
}
