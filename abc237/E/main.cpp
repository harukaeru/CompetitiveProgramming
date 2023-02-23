#include <bits/stdc++.h>

using namespace std;

int main() {
  int N, M;
  cin >> N >> M;
  vector<int> H(N);
  for (int i = 0; i < N; i++) {
    cin >> H[i];
  }

  vector<unordered_map<int, long long>> G(N);
  for (int i = 0; i < M; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    if (H[u] <= H[v]) {
      swap(u, v);
    }
    if (!G[u].count(v)) {
      G[u][v] = -(H[u] - H[v]);
      G[v][u] = 2 * (H[u] - H[v]);
    }
  }

  vector<long long> dists(N, 1e18);
  dists[0] = 0;
  priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
  pq.push({0, 0});
  while (!pq.empty()) {
    auto [score, u] = pq.top();
    pq.pop();
    if (dists[u] > score) {
      continue;
    }
    for (auto [v, v_cost] : G[u]) {
      if (dists[u] + v_cost < dists[v]) {
        dists[v] = dists[u] + v_cost;
        pq.push({dists[v], v});
      }
    }
  }

  cout << -*min_element(dists.begin(), dists.end()) << endl;

  return 0;
}
