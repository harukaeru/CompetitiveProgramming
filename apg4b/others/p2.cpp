#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

int sum(int n) {
  if (n == 0) {
    return 0;
  }

  return n + sum(n - 1);
}
int main() {
  cout << sum(10) << endl;
}