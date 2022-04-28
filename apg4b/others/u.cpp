#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

// int sum100(vector<int> a) {
int sum100(vector<int> &a) {
  int result = 0;
  for (int i = 0; i < 100; i++) {
    result += a.at(i);
  }
  return result;
}

int main() {
  vector<int> a(1000000000, 1);

  rep(i, 500) {
    cout << sum100(a) << endl;
  }
}