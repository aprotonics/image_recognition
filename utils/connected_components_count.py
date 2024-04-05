
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


def connected_components_count(graph):
    graph = graph
    
    visited = set()
    connected_components_count = 0
    triangles_areas_list = []
    graph_list = []
    area_is_empty = True

    for key in graph.edges.keys():
        if key not in visited:

            new_graph, visited = depth_first_search(graph.edges, key, visited)

            if not area_is_empty:
                graph_list.extend(triangles_areas_list[connected_components_count-1])
                
                graph_set = set(graph_list)
                new_graph_set = set(new_graph)

                filtered_set = new_graph_set.difference(graph_set)
                filtered_graph = list(filtered_set)
                triangles_areas_list.append(filtered_graph)

            if area_is_empty:
                graph_list = []
                
                triangles_areas_list.append(new_graph)
                area_is_empty = False

            connected_components_count += 1

    return connected_components_count, triangles_areas_list
