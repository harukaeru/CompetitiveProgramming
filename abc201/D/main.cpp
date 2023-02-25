#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int H, W;
char A[4005][4005];
long long memo[4005][4005];

long long dfs(int y, int x) {
  if (memo[y][x]) {
    return memo[y][x];
  }

  int takahashi = (x + y) % 2;
  if (y == H - 1 && x == W - 1) {
    memo[y][x] = 0;
    return 0;
  }

  if (takahashi == 0) {
    memo[y][x] = -1e18;
    if (y < H - 1) {
      memo[y][x] = max(memo[y][x], dfs(y + 1, x) + (A[y + 1][x] == '+' ? 1 : -1));
    }
    if (x < W - 1) {
      memo[y][x] = max(memo[y][x], dfs(y, x + 1) + (A[y][x + 1] == '+' ? 1 : -1));
    }
    return memo[y][x];
  } else {
    memo[y][x] = 1e18;
    if (y < H - 1) {
      memo[y][x] = min(memo[y][x], dfs(y + 1, x) + (A[y + 1][x] == '+' ? -1 : 1));
    }
    if (x < W - 1) {
      memo[y][x] = min(memo[y][x], dfs(y, x + 1) + (A[y][x + 1] == '+' ? -1 : 1));
    }
    return memo[y][x];
  }
}

int main() {
  cin >> H >> W;
  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      cin >> A[i][j];
    }
  }

  long long ans = dfs(0, 0);
  if (ans > 0) {
    cout << "Takahashi" << endl;
  } else if (ans == 0) {
    cout << "Draw" << endl;
  } else {
    cout << "Aoki" << endl;
  }
  return 0;
}
