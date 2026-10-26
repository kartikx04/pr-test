import heapq

def min_cost_max_flow(graph, source, sink, n):
    flow = 0
    total_cost = 0

    while True:
        dist = [float("inf")] * n
        parent = [-1] * n
        dist[source] = 0
        pq = [(0, source)]

        while pq:
            d, u = heapq.heappop(pq)

            if d != dist[u]:
                continue

            for v, capacity, cost in graph[u]:
                if capacity > 0:
                    new_dist = d + cost

                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        parent[v] = u
                        heapq.heappush(pq, (new_dist, v))

        if parent[sink] == -1:
            break

        path_cost = dist[sink]
        v = sink

        while v != source:
            u = parent[v]

            for edge in graph[u]:
                if edge[0] == v:
                    edge[1] -= 1
                    break

            v = u

        flow += 1
        total_cost += path_cost

    return flow, total_cost
