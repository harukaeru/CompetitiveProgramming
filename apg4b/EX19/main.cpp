#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

void saiten(vector<vector<int>> &A, int &correct_count, int &wrong_count) {
  rep(i, 9) {
    int left = i + 1;
    rep(j, 9) {
      int right = j + 1;
      int a_answer = A.at(i).at(j);
      int correct_answer = left * right;
      if (a_answer == correct_answer) {
        correct_count++;
      } else {
        wrong_count++;
        A.at(i).at(j) = correct_answer;
      }
    }
  }
}

int main() {
  // A君の回答を受け取る
  vector<vector<int>> A(9, vector<int>(9));
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      cin >> A.at(i).at(j);
    }
  }

  int correct_count = 0; // ここに正しい値のマスの個数を入れる
  int wrong_count = 0;   // ここに誤った値のマスの個数を入れる

  // A, correct_count, wrong_countを参照渡し
  saiten(A, correct_count, wrong_count);

  // 正しく修正した表を出力
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      cout << A.at(i).at(j);
      if (j < 8)
        cout << " ";
      else
        cout << endl;
    }
  }
  // 正しいマスの個数を出力
  cout << correct_count << endl;
  // 誤っているマスの個数を出力
  cout << wrong_count << endl;
}