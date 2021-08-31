from graphviz import Digraph
import datetime
import csv
import io

edge_seeds = []
while 1:
    try:
        edge_seeds.append(input())
    except Exception as e:
        break

edges = []
for seed in edge_seeds:
    if '→' not in seed:
        edges.append(['S', seed])
    else:
        edges.append(list(seed.split('→')))

data = {}
G = Digraph(format="png")
G.attr("node", shape="square", style="filled", width='2', fixedsize='true')
#
# reader = csv.DictReader(f, fieldnames=headers, delimiter='\t')
# dmz = []
# for row in reader:
#     dmz.append(row)

def create_node(G, name):
    if name == 'S':
        G.node(name, shape='circle', pos='3,3!')
        return
    G.node(name, shape='circle')

def create_edge(G, v1, v2):
    G.edge(v1, v2)

existing_nodes = set()
print('edges', edges)
for edge in edges:
    print('edge', edge)
    v1, v2 = edge
    if v1 not in existing_nodes:
        create_node(G, v1)
    if v2 not in existing_nodes:
        create_node(G, v2)
    create_edge(G, v1, v2)

G.render('outimage')
# for row in dmz + dmz:
#     print('f_row', row)
#     p_rows = filter(lambda r: r['No'] == row['先行タスク'], dmz)
#     p_rows = list(p_rows)
#     if not p_rows:
#         row['最速開始時刻'] = now
#         row['待ち時間'] = 0
#         continue
#     p_row = p_rows[0]
#     el = p_row['所要時間']
#     sp = list(map(int, el.split(':')))
#     td = datetime.timedelta(hours=sp[0], minutes=sp[1])
#
#     row['最速開始時刻'] = p_row.get('最速開始時刻', now) + td
#     row['待ち時間'] = p_row.get('所要時間')
#
# for row in dmz:
#     t = row['タイトル']
#     print('row', row)
#     tt = row['最速開始時刻'].strftime('%H:%M') + '\n'
#     for i in range(len(t)):
#         tt += t[i]
#         if i != 0 and i % 8 == 0:
#             tt += '\n'
#
#     G.node(row['No'], shape='circle', color=get_color(row['No']), label=tt)
#     G.edge(row['先行タスク'], row['No'], label=str(row['待ち時間']))

