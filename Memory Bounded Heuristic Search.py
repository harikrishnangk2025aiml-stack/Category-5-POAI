def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal = state[i] - 1
            distance += abs(i // 3 - goal // 3)
            distance += abs(i % 3 - goal % 3)

    return distance

def ida_star(start, goal):
    path = [start]
    limit = heuristic(start)

    def search(g, limit):
        state = path[-1]
        f = g + heuristic(state)

        if f > limit:
            return f

        if state == goal:
            return True

        minimum = float('inf')
        zero = state.index(0)

        for move in [-3, 3, -1, 1]:
            new = zero + move

            if new < 0 or new >= 9:
                continue

            if move == -1 and zero % 3 == 0:
                continue
            if move == 1 and zero % 3 == 2:
                continue

            next_state = list(state)
            next_state[zero], next_state[new] = next_state[new], next_state[zero]
            next_state = tuple(next_state)

            if next_state not in path:
                path.append(next_state)

                result = search(g + 1, limit)

                if result == True:
                    return True

                minimum = min(minimum, result)
                path.pop()

        return minimum

    while True:
        result = search(0, limit)

        if result == True:
            print("Solution:")
            for state in path:
                print(state)
            return

        if result == float('inf'):
            print("No Solution")
            return

        limit = result

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

ida_star(start, goal)