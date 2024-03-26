
graph = {
    'S': [('A', 8), ('C', 4)],
    'A': [('B', 2), ('C', 3), ('S', 8)],
    'B': [('D', 1), ('A', 2)],
    'C': [('D', 7), ('S', 4), ('A', 3)],
    'D': [('G', 6), ('B', 1), ('C', 7)],
    'G': []
}


heuristic = {'S': 10, 'A': 6, 'B': 4, 'C': 8, 'D': 5, 'G': 0}
def a_star_search(graph, heuristic, start, goal):
    open_set = [(0 + heuristic[start], 0, start, [start])]
    visited = set()

    while open_set:
        open_set.sort(key=lambda x: x[0])
        _, g, current, path = open_set.pop(0)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path, g

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                open_set.append((new_f, new_g, neighbor, path + [neighbor]))

    return None, None

path, cost = a_star_search(graph, heuristic, 'S', 'G')
print(f"Path: {path}, Cost: {cost}")
