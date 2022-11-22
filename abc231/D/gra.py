from graphviz import Digraph

# 有向グラフのインスタンス化
g = Digraph()

# 属性の指定
g.attr('node', shape='circle')

# エッジの追加
N, M = map(int, input().split())
for i in range(M):
    a, b = map(int, input().split())
    g.edge(str(a), str(b), str(a) + '~' + str(b))

# 出力
g.view()
