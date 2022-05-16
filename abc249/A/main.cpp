#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int A, B, C, D, E, F, X;
  cin >> A >> B >> C >> D >> E >> F >> X;

  int takahashi = X / (A + C) * (A * B);
  int rest_t = X % (A + C);
  takahashi += (rest_t <= A) ? rest_t * B : A * B;

  int aoki = X / (D + F) * (D * E);
  int rest_a = X % (D + F);
  aoki += (rest_a <= D) ? rest_a * E : D * E;

  if (takahashi == aoki) {
    cout << "Draw" << endl;
  } else if (takahashi > aoki) {
    cout << "Takahashi" << endl;
  } else {
    cout << "Aoki" << endl;
  }

  return 0;
}
