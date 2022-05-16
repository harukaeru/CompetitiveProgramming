#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  long N;
  cin >> N;

  long l = 1;
  long u = 1;
  int count = 31;

  while (count > 0) {
    l *= (-2);
    u *= 2;
    count--;
  }

  if (l <= N && N < u) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }

  return 0;
}
