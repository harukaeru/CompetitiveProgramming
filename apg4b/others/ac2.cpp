#include <bits/stdc++.h>
// #include <bitset>
// #include <iostream>
// #include <vector>

using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

int main() {
  vector<int> a = {1, 2, 3, 5, 7};
  vector<int> b = {1, 3, 5, 7};

  bitset<8> a_bitset;
  bitset<8> b_bitset;
  rep(i, a.size()) {
    int v = a.at(i);
    a_bitset.set(v - 1, 1);
  }
  rep(i, b.size()) {
    int v = b.at(i);
    b_bitset.set(v - 1, 1);
  }

  bitset<8> common_bitset = a_bitset & b_bitset;

  rep(i, 8) {
    int flag = common_bitset.test(i);
    if (flag) {
      int v = i + 1;
      cout << v << endl;
    }
  }

  bitset<4> x("1010");

  cout << x << endl;
}