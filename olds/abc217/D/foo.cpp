#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define pb push_back
#define push_back emplace_back
#define Good_Bye_amano_hina cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
#define bp __builtin_popcount
typedef long long ll;
typedef unsigned long long ull;

int main()
{
    ll L;
    ll Q;
    ll c_i;
    ll x_i;
    cin >> L >> Q;
    vector<long long> keys(Q);
    for (ll i = 0; i < Q; i++) {
        keys[i] = 99999999999;
    }
    keys[1] = L;

    for (ll i = 0; i < Q; i++) {
        cin >> c_i >> x_i;
        if (c_i == 1) {
           ll pos = std::binary_search(keys.begin(), keys.end(), x_i);

           keys.insert(keys.begin() + pos, x_i);
        } else {
           ll pos = std::binary_search(keys.begin(), keys.end(), x_i);
           ll k = keys[pos];
           if (pos - 1 < 0) {
               cout << k << endl;
           } else {
               cout << (k - keys[pos - 1]) << endl;
           }
        }
     }
 }
