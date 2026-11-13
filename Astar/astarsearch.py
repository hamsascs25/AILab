
import heapq

# Graph with edge costs
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'C': 2, 'D': 5},
    'B': {'D': 1},
    'C': {'G': 3},
    'D': {'G': 2},
    'G': {}
}

# Heuristic values
h = {
    'S': 5,
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 2,
    'G': 0
}

def a_star(start, goal):

    open_list = []
    heapq.heappush(open_list, (h[start], start))

    g = {start: 0}
    parent = {start: None}

    step = 1

    while open_list:

        f, current = heapq.heappop(open_list)

        print("\nStep", step)
        print("Current Node:", current)
        print("g(n):", g[current])
        print("h(n):", h[current])
        print("f(n):", f)

        step += 1

        # Check goal
        if current == goal:
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()

            print("\nGoal Reached!")
            print("Optimal Path:", " -> ".join(path))
            print("Total Cost:", g[goal])
            return

        # Expand neighbours
        for neighbour, cost in graph[current].items():

            new_g = g[current] + cost
            new_f = new_g + h[neighbour]

            print("Neighbour:", neighbour,
                  "g =", new_g,
                  "h =", h[neighbour],
                  "f =", new_f)

            if new_g < g.get(neighbour, float('inf')):

                g[neighbour] = new_g
                parent[neighbour] = current

                heapq.heappush(
                    open_list,
                    (new_f, neighbour)
                )

    print("Goal not reachable")


# Initial and Goal states
initial_state = 'S'
goal_state = 'G'

print("A* SEARCH ALGORITHM")
print("Initial State:", initial_state)
print("Goal State:", goal_state)

a_star(initial_state, goal_state)
