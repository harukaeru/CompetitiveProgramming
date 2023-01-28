#!/usr/bin/env pypy3
N = int(input())
S = []
for i in range(N):
  S.append(input())

class Node:
  def __init__(self, x, v):
    self.x = x
    self.children = {}
    self.counter = 1

  def __repr__(self):
    return f'<[{self.s}]: {self.x}: {self.children.items()}>'


root = Node(None, None)
for v, s in enumerate(S):
  check_node = root
  for i in range(len(s)):
    child_node = check_node.children.get(s[i])
    if child_node:
      check_node = child_node
      check_node.counter += 1
      continue
    new_node = Node(s[i], v)
    check_node.children[s[i]] = new_node
    check_node = new_node

for v, s in enumerate(S):
  check_node = root
  vv = set([v])
  cnt = 0
  for i in range(len(s)):
    check_node = check_node.children.get(s[i])
    if check_node.counter <= 1:
      break
    cnt += 1
  print(cnt)