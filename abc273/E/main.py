#!/usr/bin/env pypy3
Q = int(input())

class Node:
  def __init__(self, parent, v):
    self.parent = parent
    self.v = v

root = Node(None, -1)
curNode = root

anses = []
notes = {}
for i in range(Q):
  cmd, *data = input().split()
  if cmd == 'ADD':
    v = data[0]
    curNode = Node(curNode, v)
    anses.append(curNode.v)
  elif cmd == 'DELETE':
    if curNode.parent:
      curNode = curNode.parent
    anses.append(curNode.v)
  elif cmd == 'SAVE':
    pos = data[0]
    notes[pos] = curNode
    anses.append(curNode.v)
  elif cmd == 'LOAD':
    pos = data[0]
    curNode = notes.get(pos, root)
    anses.append(curNode.v)

# print(notes)
print(*anses)