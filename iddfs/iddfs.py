def dls(graph, node, goal, depth):
    if node == goal:
        return True

    if depth == 0:
        return False

    for neighbor in graph[node]:
        if dls(graph, neighbor, goal, depth - 1):
            return True

    return False


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print("Depth limit:", depth)

        if dls(graph, start, goal, depth):
            print("Goal found:", goal)
            return True

    print("Goal not found")
    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

iddfs(graph, 'A', 'G', 2)
