class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the graph's adjacency list
        self.graph = {}
    
    def add_node(self, node):
        # Add a new node to the graph with an empty list of neighbors
        self.graph[node] = []
    
    def add_edge(self, start, end):
        # Ensure nodes exist and then add a directed edge from start to end
        if start not in self.graph:
            self.add_node(start)
        if end not in self.graph:
            self.add_node(end)
        # Append end to the list of neighbors for the start node
        self.graph[start].append(end)

    def print_adjacency_list(self):
        # Print the adjacency list of the graph
        for node, neighbors in self.graph.items():
            print(f'{node} -> {neighbors}')
    
    def dfs(self, start, visited=None):
        # Perform Depth-First Search starting from the given node
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example Usage:
graph = Graph()

# Adding nodes
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")

# Adding directed edges
graph.add_edge("A", "E")
graph.add_edge("B", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "A")

# Printing the adjacency list
print("Adjacency List:")
graph.print_adjacency_list()

# Performing DFS starting from node "B"
print("\nDFS:")
graph.dfs("B")
