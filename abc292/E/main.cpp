#include <iostream>
#include <queue>
#include <unordered_set>
#include <vector>

using namespace std;

int main() {
  int N, M;
  cin >> N >> M;

  vector<unordered_set<int>> G(N);
  for (int i = 0; i < M; i++) {
    int u, v;
    cin >> u >> v;
    u -= 1;
    v -= 1;
    G[u].insert(v);
  }

  int cnt = 0;
  for (int i = 0; i < N; i++) {
    unordered_set<int> seen;
    queue<int> q;
    q.push(i);
    while (!q.empty()) {
      int v = q.front();
      q.pop();
      if (seen.count(v)) {
        continue;
      }
      seen.insert(v);

      for (auto nex : G[v]) {
        if (seen.count(nex)) {
          continue;
        }
        if (G[i].count(nex)) {
          q.push(nex);
        } else {
          // cout << "?" << " " << i << " " << nex << endl;
          G[i].insert(nex);
          cnt += 1;
          q.push(nex);
        }
      }
    }
  }

  cout << cnt << endl;

  return 0;
}