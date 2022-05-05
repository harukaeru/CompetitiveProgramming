#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (int)n; i++)

int main() {
  for (int tmp = 0; tmp < (1 << 10); tmp++) {
    bitset<10> s(tmp);
    cout << s << endl;
  }
}