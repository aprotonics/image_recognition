class Queue:
    def __init__(self):
        self.elements = []
    
    def length(self):
        return self.elements.__len__()

    def empty(self):
        return self.elements.__len__() == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.pop(0)


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def length(self):
        return self.elements.__len__()
    
    def empty(self):
        return self.elements.__len__() == 0

    def put(self, x, priority):
        self.elements.append((x, priority))
    
    def get(self):
        min_priority = 10000

        if self.length() > 0:
            min_priority = self.elements[0][1]

        for i in range(len(self.elements)):
            if self.elements[i][1] < min_priority:
                min_priority = self.elements[i][1]

        for i in range(len(self.elements)):
            if self.elements[i][1] == min_priority:
                value = self.elements[i][0]
                self.elements.remove((value, min_priority))
                return value


def breadth_first_search1(graph, start):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()

        for next in graph.nears(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

def breadth_first_search2(graph, start, img, quality):
    graph = graph
    start = start
    img = img
    quality = quality

    graph_area = []
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    
    while not frontier.empty():
        current = frontier.get()

        (x, y) = current
        if check_not_in_bounds((y, x), img):
            if img[y, x, 0] < 100 - quality and\
                img[y, x, 1] < 100 - quality and\
                img[y, x, 2] < 100 - quality:
                graph_area.append(current)

        for next in graph.nears(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True
    
    return graph_area

async def breadth_first_search2_async(graph, start, img, quality):
    graph = graph
    start = start
    img = img
    quality = quality

    graph_area = []
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    
    while not frontier.empty():
        current = frontier.get()

        (x, y) = current
        if check_not_in_bounds((y, x), img):
            if img[y, x, 0] < 100 - quality and\
                img[y, x, 1] < 100 - quality and\
                img[y, x, 2] < 100 - quality:
                graph_area.append(current)

        for next in graph.nears(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True
    
    return graph_area

def breadth_first_search3(graph, start):
    graph = graph
    start = start
    
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    priority = {}
    came_from[start] = None
    priority[start] = 0
    height_to_width_ratio = graph.height_to_width_ratio

    while not frontier.empty():
        current = frontier.get()

        for near in graph.nears(current):
            new_priority = priority[current] + heuristic(height_to_width_ratio, (current, near))
            if near not in came_from:
                priority[near] = new_priority
                frontier.put(near, new_priority)
                came_from[near] = current

def breadth_first_search4(graph, start, img, quality):
    graph = graph
    start = start
    img = img
    quality = quality
    
    graph_area = []
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    priority = {}
    came_from[start] = None
    priority[start] = 0
    height_to_width_ratio = graph.height_to_width_ratio

    while not frontier.empty():
        current = frontier.get()

        (x, y) = current
        if img[y, x, 0] < 100 - quality and\
            img[y, x, 1] < 100 - quality and\
            img[y, x, 2] < 100 - quality:
            graph_area.append(current)

        for near in graph.nears(current):
            new_priority = priority[current] + heuristic(height_to_width_ratio, (current, near))
            if near not in came_from:
                priority[near] = new_priority
                frontier.put(near, new_priority)
                came_from[near] = current

    return graph_area

def breadth_first_search5(graph, start, img, quality):
    graph = graph
    start = start
    img = img
    quality = quality

    print(start)

    graph_area = []
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    
    while not frontier.empty():
        current = frontier.get()

        (x, y) = current

        if img[y][x][0] > 255 - (100 - quality) and\
            img[y][x][1] > 255 - (100 - quality) and\
            img[y][x][2] > 255 - (100 - quality):
            graph_area.append(current)

        for next in graph.nears(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True
    
    return graph_area

def breadth_first_search6(graph, start, img, quality):
    graph = graph
    start = start
    img = img
    quality = quality
    
    graph_area = []
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    priority = {}
    came_from[start] = None
    priority[start] = 0
    height_to_width_ratio = graph.height_to_width_ratio

    while not frontier.empty():
        current = frontier.get()

        (x, y) = current
        if img[y, x, 0] > 255 - (100 - quality) and\
            img[y, x, 1] > 255 - (100 - quality) and\
            img[y, x, 2] > 255 - (100 - quality):
            graph_area.append(current)

        for near in graph.nears(current):
            new_priority = priority[current] + heuristic(height_to_width_ratio, (current, near))
            if near not in came_from:
                priority[near] = new_priority
                frontier.put(near, new_priority)
                came_from[near] = current

    return graph_area

def heuristic(height_to_width_ratio, line):
    
    vector_distance = abs(abs(line[1][1] - line[0][1]) - abs(line[1][0] - line[0][0]))

    value = 0
    if (line[1][1] - line[0][1]) == 0:
        value = height_to_width_ratio[0]
    if (line[1][0] - line[0][0]) == 0:
        value = height_to_width_ratio[1]
    if (line[1][1] - line[0][1]) != 0 and (line[1][0] - line[0][0]) != 0:
        value = height_to_width_ratio[0] * height_to_width_ratio[1]

    return vector_distance * value

def check_not_in_bounds(coordinates, img):
    (x, y) = coordinates
    width = img.shape[0]
    height = img.shape[1]

    return 0 <= x < width and 0 <= y < height
