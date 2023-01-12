#include <iostream>
#include <vector>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int T;
  cin >> T;
  rep(i, T) {
    int N, S;
    cin >> N >> S;
    vector<int> A(N);
    rep(j, N) {
      cin >> A.at(j);
    }

    int r = 0;
    int tot = 0;
    int minLength = N + 1;

    rep(l, N) {
      // 越える直前までrをインクリメント
      while (r < N && tot + A.at(r) < S) {
        tot += A.at(r);
        r++;
      }

      // 越えるなら越えさせる
      if (r < N && tot < S && tot + A.at(r) >= S) {
        tot += A.at(r);
        r++;
      }

      // cout << "(" << l << "," << r << ") -> " << tot << endl;
      // cout << "S: " << S << endl;
      if (tot >= S) {
        // cout << "   (l,r)" << l << "," << r << endl;
        minLength = min(minLength, r - l);
      }

      if (l == r) {
        r += 1;
      }

      // 左端を取り除く
      tot -= A.at(l);
    }

    if (minLength == N + 1) {
      minLength = 0;
    }

    cout << minLength << endl;
  }

  return 0;
}
