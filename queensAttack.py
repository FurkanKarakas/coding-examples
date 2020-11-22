def queensAttack(n, k, r_q, c_q, obstacles):
    u = n - r_q
    d = r_q-1
    r = n - c_q
    l = c_q-1
    ru = min(u, r)
    rd = min(r, d)
    lu = min(l, u)
    ld = min(l, d)
    # For each obstacle, determine its position relative to the queen and update the reachable region by taking the minimum.
    # Note that by taking minimum, we don't need to consider the cases where an obstacle is made useless by staying behind another obstacle.
    # I.e., the minimum case automatically handles those situations.
    for r_o, c_o in obstacles:
        # Down
        if c_o == c_q and r_o < r_q:
            d = min(d, r_q-1-r_o)
        # Up
        elif c_o == c_q and r_o > r_q:
            u = min(u, r_o-r_q-1)
        # Left
        elif r_o == r_q and c_o < c_q:
            l = min(l, c_q-1-c_o)
        # Right
        elif r_o == r_q and c_o > c_q:
            r = min(r, c_o-c_q-1)
        # Right-up
        elif c_o-c_q == r_o-r_q and c_o > c_q:
            ru = min(ru, c_o-c_q-1)
        # Left-down
        elif c_o-c_q == r_o-r_q and c_o < c_q:
            ld = min(ld, c_q-1-c_o)
        # Left-up
        elif c_o-c_q == -r_o+r_q and r_o > r_q:
            lu = min(lu, r_o-r_q-1)
        # Right-down
        elif c_o-c_q == -r_o+r_q and r_o < r_q:
            rd = min(rd, r_q-1-r_o)

    return u + d + r + l + ru + rd + lu + ld


if __name__ == '__main__':
    n, k = 5, 3
    r_q, c_q = 4, 3
    obstacles = [[5, 5], [4, 2], [2, 3]]
    result = queensAttack(n, k, r_q, c_q, obstacles)
    assert result == 10
    print(result)
