#include <bits/stdc++.h>
#include <numeric>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N, X;
  cin >> N >> X;

  vector<int> vec(N);
  rep(i, N) {
    cin >> vec.at(i);
  }

  int s = accumulate(vec.begin(), vec.end(), 0);
  int min_m = *min_element(vec.begin(), vec.end());

  int rest = (X - s) / min_m;

  cout << rest + N << endl;

  return 0;
}
