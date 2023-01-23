import heapq

def dijkstra(start):
  p_queue = [(0, start)]

  dists = [1e18] * N
  dists[start] = 0

  while len(p_queue) > 0:
    d, current_node = heapq.heappop(p_queue)
    # 別になくても動くけど、priority_queueに同一nodeが何個も入ることがあるので、
    # 同じのが入ったときにわざわざfor文に行きたくない。そのためここでちょんぎっている
    if dists[current_node] < d:
      continue

    for d_from_current_to_nex, nex_node in G[current_node]:
      d_from_start_to_nex = d_from_current_to_nex + dists[current_node]
      if dists[nex_node] > d_from_start_to_nex:
        dists[nex_node] = d_from_start_to_nex
        heapq.heappush(p_queue, (d_from_start_to_nex, nex_node))
  return dists


