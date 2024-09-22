def solution(L):
    n = len(L)
    m = len(L[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    dp = [[[float('inf') for _ in range(2)] for _ in range(m)] for _ in range(n)]

    queue = [(0, 0, 0, 0)]  # (x, y, wall breaks, distance)

    dp[0][0][0] = 0

    while queue:
        x, y, walls, distance = queue.pop(0)

        if x == n - 1 and y == m - 1:
            return distance+1

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < n and 0 <= new_y < m:
                newWalls = walls + L[new_x][new_y]

                if newWalls <= 1:
                    newDistance = distance + 1

                    if newDistance < dp[new_x][new_y][newWalls]:
                        dp[new_x][new_y][newWalls] = newDistance
                        queue.append((new_x, new_y, newWalls, newDistance))


# Test cases
assert solution([[0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1],
                 [0, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0]]) == 11

assert solution([[0, 1, 1, 0],
                 [0, 0, 0, 1],
                 [1, 1, 0, 0],
                 [1, 1, 1, 0]]) == 7
