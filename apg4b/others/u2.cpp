#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

int op_double(int i) { return i * 2; }

int main() {
  vector<int> vec = {1, 2, 3, 4, 5};

  transform(vec.begin(), vec.end(), vec.begin(), op_double);

  for (int v : vec) {
    cout << v << endl;
  }
}