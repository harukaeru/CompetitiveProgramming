#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int H, W, R, C;
  cin >> H >> W >> R >> C;

  int cnt = 4;
  if (R == 1)
    cnt--;
  if (R == H)
    cnt--;
  if (C == 1)
    cnt--;
  if (C == W)
    cnt--;

  cout << cnt << endl;

  return 0;
}
