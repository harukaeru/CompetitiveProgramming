#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> a = {1, 3, 4, 5, 9, 10};
  // 偶数であるような最初の要素を指すイテレータ
  auto itr = find_if(a.begin(), a.end(), [](int x) { return (x % 2 == 0); });
  if (itr == a.end()) {
    cout << "not found" << endl;
  } else {
    cout << *itr << endl;
  }
}
