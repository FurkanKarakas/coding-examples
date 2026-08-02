class UnionFind:
    def __init__(self, size: int) -> None:
        self.size = size
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p: int) -> int:
        """
        Recursively finds the root of the element p and applies path compression to optimize future queries.
        """
        if not 0 <= p <= self.size-1:
            raise ValueError(
                f"Element {p} is out of bounds for UnionFind of size {self.size}.")

        # If this node is not the root, recursively find the root and compress the path
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p: int, q: int) -> bool:
        """
        Connects the elements p and q. Returns True if they were not already connected, False otherwise."""
        if not 0 <= p <= self.size-1 or not 0 <= q <= self.size-1:
            raise ValueError(
                f"Elements {p} and/or {q} are out of bounds for UnionFind of size {self.size}.")

        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return False  # Already connected

        # Union by rank
        if self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
            self.rank[rootQ] += self.rank[rootP]
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += self.rank[rootQ]

        return True

    def num_components(self) -> int:
        """
        Returns the number of connected components in the Union-Find structure.
        """
        return sum(1 for i in range(self.size) if self.find(i) == i)


if __name__ == "__main__":
    uf = UnionFind(10)
    print(uf.union(0, 1))  # True
    print(uf.union(1, 2))  # True
    print(uf.find(0))      # Should return the root of the set containing 1
    print(uf.find(2))      # Should return the root of the set containing 3
    print(uf.union(0, 2))  # False, since they are already connected
    # Should return the number of connected components
    print(uf.num_components())
