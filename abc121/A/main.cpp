#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int H, W;
  int h, w;
  cin >> H >> W;
  cin >> h >> w;

  cout << H * W - h * W - w * H + h * w << endl;
  return 0;
}
