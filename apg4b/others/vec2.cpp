#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < n; i++)

int main() {
  vector<int> vec = {1, 2, 3};

  vec.push_back(10);

  rep(i, vec.size()) {
    cout << vec.at(i) << endl;
  }
}