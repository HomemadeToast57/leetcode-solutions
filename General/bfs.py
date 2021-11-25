graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# breadth field search for graph


def bfs(graph, source):
    queue = [source]

    while queue:
        current = queue.pop(0)
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)


bfs(graph, 'a')  # a, c, b, e, d, f
