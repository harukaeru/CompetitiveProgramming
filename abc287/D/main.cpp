#include <iostream>
#include <string>

int main() {
  std::string S, T;
  std::cin >> S >> T;

  for (int x = 0; x <= (int)T.length(); x++) {
    int p = T.length() - x;
    std::string xx = S.substr(0, x);
    std::string yy = (p > 0) ? S.substr((int)S.length() - p) : "";
    std::string s = xx + yy;
    bool ng = false;
    for (int i = 0; i < (int)T.length(); i++) {
      if (s[i] == T[i])
        continue;
      if (s[i] == '?' || T[i] == '?')
        continue;

      ng = true;
      break;
    }
    if (ng) {
      std::cout << "No" << std::endl;
    } else {
      std::cout << "Yes" << std::endl;
    }
  }
  return 0;
}