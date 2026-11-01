"""Prim's algorithm for finding the Minimum Spanning Tree (MST) of a graph."""

import heapq


def prim(V: int, edges: list[tuple[int, int, int]], src: int = 0) -> list[tuple[int, int, int]]:
    """Find the Minimum Spanning Tree (MST) of a graph using Prim's algorithm."""
    adj = [[] for _ in range(V)]
    for u, v, wt in edges:
        adj[u].append((v, wt))
        adj[v].append((u, wt))

    mst = []
    visited = [False] * V
    minHeap = [(0, src, -1)]  # (weight, current_node, parent_node)

    while minHeap and len(mst) < V - 1:
        wt, u, parent = heapq.heappop(minHeap)
        if visited[u]:
            continue
        visited[u] = True
        if parent != -1:
            mst.append((parent, u, wt))
        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(minHeap, (w, v, u))

    return mst


if __name__ == '__main__':
    V = 5
    edges = [(1, 3, 2), (4, 3, -1), (2, 4, 1), (1, 2, 1), (0, 1, 5)]
    src = 0
    mst = prim(V, edges, src)
    print(' '.join(map(str, mst)))
