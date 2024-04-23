
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


class SimpleGraph:
    def __init__(self):
        self.edges = {

        }

        self.vertices = []
    
    def nears(self, id):
        return self.edges[id]

    def nears2(self, id):
        point = id
        
        nears2 = [
                    (point[0]+1, point[1]), 
                    (point[0], point[1]+1), 
                    (point[0]-1, point[1]), 
                    (point[0], point[1]-1), 
                    (point[0]+1, point[1]+1), 
                    (point[0]-1, point[1]-1), 
                    (point[0]+1, point[1]-1), 
                    (point[0]-1, point[1]+1),
                    ]

        return nears2
    
    def nears3(self, id):
        point = id
        
        nears3 = [
                    (point[0]+1, point[1]), 
                    (point[0], point[1]+1), 
                    (point[0]-1, point[1]), 
                    (point[0], point[1]-1), 
                    (point[0]+1, point[1]+1), 
                    (point[0]-1, point[1]-1), 
                    (point[0]+1, point[1]-1), 
                    (point[0]-1, point[1]+1),
                    
                    (point[0]+2, point[1]),
                    (point[0], point[1]+2), 
                    (point[0]-2, point[1]), 
                    (point[0], point[1]-2), 
                    (point[0]+2, point[1]+2), 
                    (point[0]-2, point[1]-2), 
                    (point[0]+2, point[1]-2), 
                    (point[0]-2, point[1]+2),
                    (point[0]+1, point[1]+2),
                    (point[0]+2, point[1]+1),
                    (point[0]-1, point[1]-2),
                    (point[0]-2, point[1]-1),
                    (point[0]+1, point[1]-2),
                    (point[0]+2, point[1]-1),
                    (point[0]-1, point[1]+2),
                    (point[0]-2, point[1]+1),
                    ]

        return nears3
    
    def degree(self, id):
        edges = self.nears(id)
        degree = 0
        for key in edges.keys():
            degree += 1
        return degree
    
    def order(self):
        return len(self.vertices)


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.triangles = []
    
    def in_triangles_area(self, id):
        (x, y) = id
        
        return (x, y) in self.triangles

    def in_bounds(self, id):
        (x, y) = id

        return 0 <= x < self.width and 0 <= y < self.height
    
    def nears(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        results = filter(self.in_bounds, results)

        return results


# height to width
# 2 to 1
# 3 to 2
# 4 to 3
# 5 to 3
# 5 to 4
# 7 to 4
# 6 to 5
# 8 to 5
# 9 to 5
# 7 to 6
# 11 to 6
# 8 to 7
# 9 to 7
# 10 to 7
# 11 to 7
# 12 to 7
# 13 to 7


class RectangularGrid:
    def __init__(self, width, height, height_to_width_ratio):
        self.width = width
        self.height = height
        self.height_to_width_ratio = height_to_width_ratio

        self.height_step = self.height_to_width_ratio[0]
        self.width_step = self.height_to_width_ratio[1]
    
    def in_bounds(self, id):
        (x, y) = id

        return 0 <= x < self.width and 0 <= y < self.height

    def nears(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        results = filter(self.in_bounds, results)

        return results

