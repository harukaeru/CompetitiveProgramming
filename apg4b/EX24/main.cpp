#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

struct Clock {
  int hour;
  int minute;
  int second;

  void set(int h, int m, int s) {
    hour = h;
    minute = m;
    second = s;
  }

  string to_str() {
    string out = "";
    if (10 > hour) {
      out += '0';
    }
    out += to_string(hour);

    out += ':';
    if (10 > minute) {
      out += '0';
    }
    out += to_string(minute);

    out += ':';
    if (10 > second) {
      out += '0';
    }
    out += to_string(second);
    return out;
  }

  void shift(int diff_second) {
    int total = hour * 60 * 60 + minute * 60 + second;

    int d = (diff_second + 86400) % 86400;
    total = (total + d) % 86400;

    int total_minute = total / 60;
    second = total % 60;

    int total_hour = total_minute / 60;
    minute = total_minute % 60;

    hour = total_hour % 24;
  }
};

int main() {
  cout << -5 % 3 << endl;
  // 入力を受け取る
  int hour, minute, second;
  cin >> hour >> minute >> second;
  int diff_second;
  cin >> diff_second;

  // Clock構造体のオブジェクトを宣言
  Clock clock;

  // set関数を呼び出して時刻を設定する
  clock.set(hour, minute, second);

  // 時刻を出力
  cout << clock.to_str() << endl;

  // 時計を進める(戻す)
  clock.shift(diff_second);

  // 変更後の時刻を出力
  cout << clock.to_str() << endl;
}