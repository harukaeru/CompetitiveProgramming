#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

long long N, M;
unordered_map<long, vector<long>> G;

vector<long long> current;
unordered_set<long long> seen;

int cnt = 0;
string anstext = "";

void dfs(long v) {
  current.push_back(v);
  if ((long long)current.size() == N) {
    cnt += 1;
    if (cnt == 1) {
      vector<long> ans(N);
      for (long i = N - 1; i >= 0; i--) {
        ans[current[i]] = i + 1;
      }
      for (long i = 0; i < N; i++) {
        if (i == N - 1) {
          anstext += to_string(ans[i]);
        } else {
          anstext += to_string(ans[i]) + " ";
        }
      }
    }
  }
  if ((long long)current.size() == N + 1) {
    cout << "No" << endl;
    exit(0);
  }

  for (long nex : G[v]) {
    if (seen.find(nex) == seen.end()) {
      seen.insert(nex);
      dfs(nex);
      current.pop_back();
    }
  }
}

int main() {
  cin >> N >> M;
  for (long i = 0; i < M; i++) {
    long x, y;
    cin >> x >> y;
    x--;
    y--;
    G[x].push_back(y);
  }

  unordered_set<long> ultraseen;
  for (long i = 0; i < N; i++) {
    if (ultraseen.find(i) != ultraseen.end()) {
      continue;
    }

    seen.clear();
    seen.insert(i);
    current.clear();

    dfs(i);

    ultraseen.insert(seen.begin(), seen.end());
  }

  if (cnt == 1) {
    cout << "Yes" << endl;
    cout << anstext << endl;
    return 0;
  }

  cout << "No" << endl;
  return 0;
}
