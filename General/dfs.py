graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# depth field search for graph
def dfs(graph, source):
    stack = [ source ]
    
    while stack:
        current = stack.pop()
        print(current)
        
        for neighbor in graph[current]:
            stack.append(neighbor)
            
dfs(graph, 'a') # a, b, d, f, c, e