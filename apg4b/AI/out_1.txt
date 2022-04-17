#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> a = {1, 2, 3};
  // a.begin() .. 先頭の要素を指すイテレータ
  // a.end() .... 終端を指すイテレータ
  // it++ ....... イテレータを1つ分進める (it = it + 1と同じ)
  for (auto it = a.begin(); it != a.end(); it++) {
    cout << *it << endl;
  }
}
