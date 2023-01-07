#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <set>

using namespace std;

int N, M;
unordered_map<int, unordered_set<int>> G;
unordered_set<int> seen;
int cnt = 1;

const int P = 1e6;

void dfs(int v) {
for (auto nex : G[v]) {
if (seen.count(nex) == 0) {
seen.insert(nex);
cnt++;
if (cnt > P) {
cout << P << endl;
exit(0);
}
dfs(nex);
seen.erase(nex);
}
}
}

int main() {
cin >> N >> M;
for (int i = 0; i < M; i++) {
int u, v;
cin >> u >> v;
u--;
v--;
G[u].insert(v);
G[v].insert(u);
}

seen.insert(0);
dfs(0);
cout << min(cnt, P) << endl;

return 0;
}
