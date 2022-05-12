#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  int N;
  cin >> N;
  int x = N % 10;
  vector<int> hon = {2, 4, 5, 7, 9};
  vector<int> pon = {0, 1, 6, 8};
  if (binary_search(hon.begin(), hon.end(), x)) {
    cout << "hon" << endl;
  } else if (binary_search(pon.begin(), pon.end(), x)) {
    cout << "pon" << endl;
  } else {
    cout << "bon" << endl;
  };

  return 0;
}
