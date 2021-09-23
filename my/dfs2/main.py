G = {
    0: [1, 2, 3],
    1: [3],
    2: [3, 4],
    3: [0],
    4: [5],
    5: []
}

visited = [False] * 6

def dfs(node):
    print('node', node)
    for next_node in G[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)

visited[0] = 0
dfs(0)
