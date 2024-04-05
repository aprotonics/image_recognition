
def get_graph_result(graph, degree_cycles):
    edges = set()
    for key in graph.keys():
        values = graph[key]
        for value in values:
            edge = frozenset((key, value))
            edges.add(edge)

    vertices_degrees = {}
    for key in graph.keys():
        vertex_degree = 0
        for edge in edges:
            for node in edge:
                if node == key:
                    vertex_degree += 1
        
        vertices_degrees[key] = vertex_degree

    vertices_with_degree_1 = 0
    vertices_with_degree_2 = 0
    vertices_with_degree_3 = 0
    vertices_with_degree_4 = 0

    for next in vertices_degrees.values():
        if next == 1:
            vertices_with_degree_1 += 1
        if next == 2:
            vertices_with_degree_2 += 1
        if next == 3:
            vertices_with_degree_3 += 1
        if next == 4:
            vertices_with_degree_4 += 1

    vertices_priorities = {}
    for vertex in graph.keys():
        values = graph[vertex]
        vertex_priority = 0
        for value in values:
            vertex_priority += vertices_degrees[value]
        vertices_priorities[vertex] = vertex_priority
    
    vertices_weights = []
    for value in vertices_priorities.values():
        vertices_weights.append(value)

    vertices_priorities2 = {}
    vertices_weights2 = []

    for i in range(0, degree_cycles):
        for vertex in graph.keys():
            values = graph[vertex]
            vertex_priority = vertices_priorities[vertex]
            for value in values:
                vertex_priority += vertices_priorities[value]
            vertices_priorities2[vertex] = vertex_priority
        
        for value in vertices_priorities2.values():
            vertices_weights2.append(value)

        vertices_priorities = vertices_priorities2.copy()
        vertices_weights = vertices_weights2.copy()
        vertices_priorities2 = {}
        vertices_weights2 = []

    print()
    print()
    print()
    print(vertices_weights)
    print()

    graph_result = [len(edges), vertices_with_degree_1,
                                vertices_with_degree_2,
                                vertices_with_degree_3,
                                vertices_with_degree_4]
    
    graph_result2 = [len(edges), vertices_weights]

    graph_result3 = vertices_weights

    return graph_result2


def compare_graphs(graph1_result, graph2_result):
    edges_length1, vertices_weights1 = graph1_result
    edges_length2, vertices_weights2 = graph2_result
    list1_copy = vertices_weights1.copy()
    list2_copy = vertices_weights2.copy()
    for value in list1_copy:
        if value in list2_copy:
            list2_copy.remove(value)
        else:
            break

    if edges_length1 == edges_length2:
        if len(list2_copy) == 0:
            print("graphs are isomorphic")
        else:
            print("graphs are not isomorphic")
    else:
        print("graphs are not isomorphic")
