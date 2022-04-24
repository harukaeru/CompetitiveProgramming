#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

int main() {
  vector<int> vec = {2, 5, 2, 1};

  sort(vec.begin(), vec.end());

  rep(i, vec.size()) {
    cout << vec.at(i) << endl;
  }
}