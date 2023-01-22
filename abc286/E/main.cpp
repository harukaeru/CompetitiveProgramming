#include <iostream>
#include <map>
#include <vector>
using namespace std;

const int INF = 1e9;

int N;
vector<int> A;
vector<string> S;
map<pair<int, int>, int> dists;
map<pair<int, int>, int> vals;

int main() {
  cin >> N;
  A.resize(N);
  for (int i = 0; i < N; i++)
    cin >> A[i];
  S.resize(N);
  for (int i = 0; i < N; i++)
    cin >> S[i];

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (S[i][j] == 'Y') {
        dists[{i, j}] = 1;
        vals[{i, j}] = A[j];
      } else {
        dists[{i, j}] = INF;
        vals[{i, j}] = A[j];
      }
    }
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      for (int k = 0; k < N; k++) {
        if (dists[{j, k}] > dists[{j, i}] + dists[{i, k}]) {
          dists[{j, k}] = min(dists[{j, k}], dists[{j, i}] + dists[{i, k}]);
          vals[{j, k}] = vals[{j, i}] + vals[{i, k}];
        } else if (dists[{j, k}] == dists[{j, i}] + dists[{i, k}] && vals[{j, k}] < vals[{j, i}] + vals[{i, k}]) {
          vals[{j, k}] = vals[{j, i}] + vals[{i, k}];
        }
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

    int d = dists.count({u, v}) ? dists[{u, v}] : INF;
    if (d == INF) {
      cout << "Impossible" << endl;
      continue;
    }
    cout << d << " " << vals[{u, v}] + A[u] << endl;
  }
  return 0;
}