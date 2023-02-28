// bitDPを文系の脳みそで理解する男・実質文学科

#include <iostream>

using namespace std;
using ll = long long;

int main() {
    int N, M;
    cin >> N >> M;
    int g[N][N] = {};
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        g[a][b] = 1;
    }

    ll dp[1<<N] = {};
    dp[0] = 1; // 空集合のときトポロジカルソートの方法は1つ
    for (int A = 0; A < (1<<N); A++) { // うさぎの集合Aを０から列挙 -> すべてのうさぎを使う場合まで積み上げていく
        for (int v = 0; v < N; v++) { // v = Aから取り除くうさぎを列挙
            // Aにvが含まれているならパス(vが「Aから取り除くうさぎ」にならないので)(含まれていないなら、A=S-{v}と言える)
            if (A>>v & 1) continue;
            bool f = true; // vは一番右にくるか?こないか?
            for (int k = 0; k < N; k++) { // 他のうさぎに対して
                // kがAに含まれていて、vからkに伸びる有向辺があれば、vは集合Aで一番右に来ない
                if ((A>>k & 1) && g[v][k] == 1) f = false;
            }
            if (f) dp[A | (1<<v)] += dp[A]; // 一番右にくるならA + {v} = Sの通り数に加える(これをN回行うので総和になる)
            // ORで加算ができる
        }
    }

    cout << dp[(1<<N) - 1] << endl;

    return 0;
}
