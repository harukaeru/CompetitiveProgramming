#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, A;
  cin >> N;
  cin >> A;
  int i = 0;

  while (i < N) {
    string op;
    int B;
    cin >> op >> B;

    if (op == "+") {
      A = A + B;
    } else if (op == "-") {
      A = A - B;
    } else if (op == "*") {
      A = A * B;
    } else if (op == "/") {
      if (B == 0) {
        cout << "error" << endl;
        break;
      }
      A = A / B;
    }

    cout << i + 1 << ":" << A << endl;
    i++;
  }
  return 0;
}
