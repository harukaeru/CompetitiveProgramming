#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int)n; i++)

int main() {
  vector<int> vec = {1, 5, 7, 9, 13};

  reverse(vec.begin(), vec.end());

  rep(i, vec.size()) {
    cout << vec.at(i) << endl;
  }
}