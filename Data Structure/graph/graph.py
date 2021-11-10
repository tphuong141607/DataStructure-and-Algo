class Graph: 
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {} 
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end) 
            else:
                self.graph_dict[start] = [end]
        
        # print("Graph dict:", self.graph_dict)

    def get_paths(self, start, end, path=[]): 
        path = [*path, start] # Must return a new list, we can't change the list in place!

        if start == end: 
            return path

        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]: 
            if node not in path: 
                new_path = self.get_paths(node, end, path)
                for p in new_path: 
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = [*path, start]
        if start == end: 
            return path

        if start not in self.graph_dict:
            return None  

        shortest_path = None
        for node in self.graph_dict[start]: 
            if node not in path: 
                shortest_p = self.get_shortest_path(node, end, path)
                if shortest_p: 
                    if shortest_path is None or len(shortest_p) < len(shortest_path): 
                        shortest_path = shortest_p
     
        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"

    # print(f"Paths between {start} and {end}: ", route_graph.get_paths(start, end))
    print(f"Shortest Paths between {start} and {end}: ", route_graph.get_shortest_path(start, end))

