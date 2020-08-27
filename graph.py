class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __str__(self):
        return f'{self.vertices}'


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

######### bft func to find the last known ancestor #########

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()           # Create empty queue and enqueue the starting_vertex
        visited = set()        # Create an empty set to track visited verticies
        
        queue.enqueue(starting_vertex)           # Add starting vertex to queue

        while queue.size() > 0:               # as long as queue is not empty run code
            popped_vertex = queue.dequeue()         #Take current vertex and pop off the queue
            if popped_vertex not in visited:      #check if it has been visisted if not print it
                print(popped_vertex)
                visited.add(popped_vertex)       #add current vertex to visisted set

            vertex_neighbors = self.get_neighbors(popped_vertex)      #use get neighbors func to get current vertex neighbors

            for n in vertex_neighbors:             #Go through each neighbor
                if n not in visited:      #if neighbor not in visited add it to the queue and we keep going
                    queue.enqueue(n)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()

        stack.push(starting_vertex)
        while stack.size() > 0:
            popped_vertex = stack.pop()
            if popped_vertex not in visited:
                print(popped_vertex)
                visited.add(popped_vertex)

                vertex_neighbors = self.get_neighbors(popped_vertex)

                for n in vertex_neighbors:
                    if n not in visited:
                        stack.push(n)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        queue = Queue()
        visited = set()
        
        queue.enqueue([starting_vertex])

        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[len(path) -1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)

            vertex_neighbors = self.get_neighbors(vertex)

            for n in vertex_neighbors:
                copy = list(path)
                copy.append(n)
                queue.enqueue(copy)