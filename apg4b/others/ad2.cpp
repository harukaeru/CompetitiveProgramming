#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

#include <pprint.hpp>

int main() {
  vector<int> v = {2, 1, 3};

  sort(v.begin(), v.end());

  do {
    for (int x : v) {
      cout << x << " ";
    }
    cout << endl;
  } while (next_permutation(v.begin(), v.end()));
}