graph = {
    'S': [('A', 8), ('C', 4)],
    'A': [('B', 2), ('C', 3), ('S', 8)],
    'B': [('D', 1), ('A', 2)],
    'C': [('D', 7), ('S', 4), ('A', 3)],
    'D': [('G', 6), ('B', 1), ('C', 7)],
    'G': []
}

class Node:
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost

    def expand(self, graph):
        return [self.child_node(graph, action) for action in graph.get(self.state, [])]

    def child_node(self, graph, action):
        next_state = action[0]
        return Node(next_state, self, self.path_cost + action[1])

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __repr__(self):
        return f"Node({self.state})"


def depth_first_search(graph, start, goal):
    frontier = [Node(start)]
    explored = set()
    
    while frontier:
        node = frontier.pop()
        if node.state == goal:
            return node.path()

        explored.add(node.state)
        for child in node.expand(graph):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
    
    return None

start_node = 'S'
goal_node = 'G'
solution_path = depth_first_search(graph, start_node, goal_node)
print("Solution Path:", solution_path)
