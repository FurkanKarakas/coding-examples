"""Kruskal's algorithm for finding the Minimum Spanning Tree (MST) of a graph."""

from union_find import UnionFind


def kruskal(V: int, edges: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    """Find the Minimum Spanning Tree (MST) of a graph using Kruskal's algorithm."""
    # Sort edges based on their weight
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(V)
    mst = []

    for u, v, wt in edges:
        if len(mst) == V - 1:
            break
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, wt))

    return mst


if __name__ == '__main__':
    V = 5
    edges = [(1, 3, 2), (4, 3, -1), (2, 4, 1), (1, 2, 1), (0, 1, 5)]
    mst = kruskal(V, edges)
    print(' '.join(map(str, mst)))
