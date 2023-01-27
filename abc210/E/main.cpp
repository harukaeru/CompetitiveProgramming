#include <algorithm>
#include <iostream>
using namespace std;

int main() {
  long N, M;
  cin >> N >> M;
  pair<long, long> edges[M];
  for (int i = 0; i < M; i++) {
    cin >> edges[i].second >> edges[i].first;
  }
  sort(edges, edges + M);

  long tot = 0;
  for (int i = 0; i < M; i++) {
    auto edge = edges[i];
    long c = edge.first, a = edge.second;
    long g = __gcd(a, N);
    tot += (N - g) * c;
    N = g;
  }

  if (N <= 1) {
    cout << tot << endl;
  } else {
    cout << -1 << endl;
  }
  return 0;
}