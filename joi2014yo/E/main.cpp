#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;

const int inf = 100000000;

int N, K;
vector<int> P, R;
map<int, vector<int>> G;
int dists_list[10005][10005];
int costs[10005];

void bfs(int pos, int s) {
  dists_list[pos][s] = 0;
  queue<int> q;
  q.push(s);
  while (!q.empty()) {
    int v = q.front();
    q.pop();
    for (int nex : G[v]) {
      if (dists_list[pos][nex] == inf) {
        dists_list[pos][nex] = dists_list[pos][v] + 1;
        q.push(nex);
      }
    }
  }
}

int main() {
  cin >> N >> K;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      dists_list[i][j] = inf;
    }
  }

  P.resize(N);
  R.resize(N);
  for (int i = 0; i < N; i++) {
    cin >> P[i] >> R[i];
  }

  for (int i = 0; i < K; i++) {
    int a, b;
    cin >> a >> b;
    a--;
    b--;
    G[a].push_back(b);
    G[b].push_back(a);
  }

  for (int i = 0; i < N; i++) {
    bfs(i, i);
    for (int j = 0; j < N; j++) {
      if (dists_list[i][j] <= R[i]) {
        dists_list[i][j] = P[i];
      } else {
        dists_list[i][j] = inf;
      }
    }
  }

  priority_queue<pair<int, int>> pq;
  for (int i = 0; i < N; i++) {
    costs[i] = inf;
  }

  costs[0] = 0;
  pq.push(make_pair(0, 0));
  while (!pq.empty()) {
    auto pp = pq.top();
    pq.pop();
    auto c = -pp.first;
    auto v = pp.second;
    if (costs[v] < c) {
      continue;
    }
    if (v == N - 1) {
      break;
    }
    for (int nex = 0; nex < N; nex++) {
      if (v == nex) {
        continue;
      }
      int nc = dists_list[v][nex];
      int nnc = c + nc;
      if (costs[nex] > nnc) {
        costs[nex] = nnc;
        pq.push(make_pair(-nnc, nex));
      }
    }
  }

  cout << costs[N - 1] << endl;
  return 0;
}