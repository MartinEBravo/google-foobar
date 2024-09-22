



def solution(src, dest):

    L = [[0 for _ in range(8)] for _ in range(8)]

    i,j = src//8,src%8
    i_m,j_m = dest//8,dest%8

    L[i_m][j_m] = 'X'
    
    dist = BFS(L, i, j)

    return dist


def BFS(L, i, j):
    moves = [(-1,2), (1,2), (-1,-2), (1,-2), (2,1), (-2,1), (2,-1), (-2,-1)]

    queue = [(i, j, 0)]
    visited = set()
    visited.add((i, j))

    while queue:
        x, y, distance = queue.pop(0)

        if L[x][y] == 'X':
            return distance

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8 and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, distance + 1))


assert solution(19,36) == 1
assert solution(0,1) == 3