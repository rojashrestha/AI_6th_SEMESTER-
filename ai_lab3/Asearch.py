

import heapq

def a_star(graph, start, goal, heuristic):
    heap = [(heuristic[start], 0, [start])]
    visited = set()

    while heap:
        f, g, path = heapq.heappop(heap)
        node = path[-1]

        if node == goal:
            return path, g

        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                new_g = g + weight
                new_f = new_g + heuristic[neighbor]
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(heap, (new_f, new_g, new_path))

    return None, float('inf')

graph_weighted = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
heuristic = {
    'A': 4,
    'B': 2,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0
}
print("A* Result:", a_star(graph_weighted, 'A', 'F', heuristic))