import heapq

def heuristic(state):
    m, c, b = state
    return (m + c + 1) // 2

def safe(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c)

def astar():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    pq = [(0, start, [start])]
    visited = set()

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while pq:
        cost, state, path = heapq.heappop(pq)

        if state == goal:
            print("Solution:")
            for p in path:
                print(p)
            return

        if state in visited:
            continue

        visited.add(state)
        m, c, b = state

        for x, y in moves:
            if b == 1:
                new = (m-x, c-y, 0)
            else:
                new = (m+x, c+y, 1)

            nm, nc, nb = new

            if safe(nm, nc) and safe(3-nm, 3-nc):
                if new not in visited:
                    g = len(path)
                    f = g + heuristic(new)
                    heapq.heappush(pq, (f, new, path + [new]))

astar()