#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

int N;
vector<int> A;
vector<string> S;
unordered_map<int, vector<int>> G;

vector<long long int> bfs(int s, int e) {
  vector<int> d(N, 1e18);
  queue<int> q;
  q.push(s);
  d[s] = 0;
  vector<int> p(N, 0);
  long long int m_cnt = 1e18;
  int point = -1;
  while (!q.empty()) {
    int v = q.front();
    q.pop();
    for (int nex : G[v]) {
      if (nex == e) {
        int reach_cnt = d[v] + 1;
        if (reach_cnt <= m_cnt) {
          m_cnt = reach_cnt;
          point = max(point, p[v] + A[nex]);
        }
        d[nex] = d[v] + 1;
        p[nex] = p[v] + A[nex];
        continue;
      } else if (d[nex] == 1e18) {
        d[nex] = d[v] + 1;
        p[nex] = p[v] + A[nex];
        q.push(nex);
      }
    }
  }
  vector<long long int> xx(2);
  xx.push_back(m_cnt);
  xx.push_back((long long int)point);
  return xx;
}

int main() {
  cin >> N;
  A.resize(N);
  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }
  S.resize(N);
  for (int i = 0; i < N; i++) {
    cin >> S[i];
  }
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (S[i][j] == 'Y') {
        G[i].push_back(j);
      }
    }
  }
  int Q;
  cin >> Q;
  for (int i = 0; i < Q; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    auto xy = bfs(u, v);
    if (xy.at(0) == 1e18) {
      cout << "Impossible" << endl;
      continue;
    }
    cout << xy.at(0) << " " << A[u] + xy.at(1) << endl;
  }
  return 0;
}