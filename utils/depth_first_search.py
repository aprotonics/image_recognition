
def depth_first_search(graph, start, visited):
    graph = graph
    start = start
    visited = visited

    stack = [start]

    while stack:
        node = stack.pop()
        visited.add(node)
        for vertex in graph[node]:
            if vertex not in visited and vertex not in stack:
                stack.append(vertex)
    
    new_graph = list(visited)

    return new_graph, visited
