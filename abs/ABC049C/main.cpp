#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main() {
  vector<string> words = {"dream", "dreamer", "erase", "eraser"};

  rep(i, words.size()) {
    reverse(words.at(i).begin(), words.at(i).end());
  }

  string S;
  cin >> S;

  reverse(S.begin(), S.end());

  for (int i = 0; i < (int)S.size();) {
    bool is_matched = false;

    rep(wi, words.size()) {
      string word = words.at(wi);

      if (S.substr(i, word.size()) == word) {
        is_matched = true;
        i += word.size();
      }
    }

    // どの単語でもマッチしなかった場合
    if (!is_matched) {
      cout << "NO" << endl;
      return 0;
    }
  }

  cout << "YES" << endl;
  return 0;
}