from heapq import heappush, heappop

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)

def heuristic(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            j = goal.index(tile)
            distance += abs(i // 3 - j // 3)
            distance += abs(i % 3 - j % 3)

    return distance


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            j = r * 3 + c
            new_state = list(state)

            new_state[zero], new_state[j] = (
                new_state[j], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def a_star(start):
    open_list = []
    heappush(open_list, (heuristic(start), 0, start))

    parent = {start: None}
    cost = {start: 0}

    while open_list:
        f, g, current = heappop(open_list)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        if g != cost[current]:
            continue

        for neighbor in get_neighbors(current):
            new_cost = g + 1

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current

                heappush(
                    open_list,
                    (new_cost + heuristic(neighbor),
                     new_cost, neighbor)
                )

    return None


def display(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()


start = (2, 8, 3,
         1, 6, 4,
         7, 0, 5)

solution = a_star(start)

if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for state in solution:
        display(state)
else:
    print("No solution exists.")
