#include <bits/stdc++.h>
#define FMT_HEADER_ONLY
#include <fmt/format.h>

int main() {
  std::string s = fmt::format("Hello, {}", 42);
  std::cout << s << std::endl;
}