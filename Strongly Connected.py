from collections import defaultdict

class Graph:
    class Node:
        def __init__(self, name):
            self.name = name
            self.edges = set()

    def __init__(self):
        self.nodemap = {}

    def AddNode(self, name):
        self.nodemap[name] = self.Node(name)

    def AddEdge(self, start, end, weight):
        self.nodemap[start].edges.add((self.nodemap[start], self.nodemap[end], weight))

    def GetAllNodes(self):
        return list(self.nodemap.values())

    def IsCircularNode(self, node):
        visited = set()
        return self._IsCircularNode(node, visited)

    def _IsCircularNode(self, node, visited):
        if node in visited:
            return True
        visited.add(node)
        for edge in node.edges:
            if self._IsCircularNode(edge[1], visited):
                return True
        visited.remove(node)
        return False

    def WrapCircularNodeInto(self, circular_node, neighbor):
        neighbor.edges.update(circular_node.edges)
        del self.nodemap[circular_node.name]

    def CountIncoming(self, node):
        count = 0
        for _, end, _ in self.GetAllEdges():
            if end == node:
                count += 1
        return count

    def GetAllEdges(self):
        edges = set()
        for node in self.GetAllNodes():
            edges.update(node.edges)
        return edges

    def PrintAdjacencyMap(self):
        for node in self.GetAllNodes():
            print(f"{node.name} -> {[edge[1].name for edge in node.edges]}")

def BuildGraph(graph, airports, routes):
    for airport in airports:
        graph.AddNode(airport)
    for route in routes:
        graph.AddEdge(route[0], route[1], 1)

def MinNewRoutes(airports, routes, starting_airport):
    graph = Graph()
    BuildGraph(graph, airports, routes)
    print("Adjacency List before wrapping circuits")
    graph.PrintAdjacencyMap()

    # Build a set of all nodes that are part of a circuit
    circulars = {node for node in graph.GetAllNodes() if graph.IsCircularNode(node)}

    # Wrap all circular nodes into one
    print("Wrapping nodes that are part of a circuit: ", end="")
    for node in circulars:
        neighbor = next(edge[1] for edge in node.edges if edge[1] in circulars)
        print(f"{node.name}, ", end="")
        graph.WrapCircularNodeInto(node, neighbor)
    print("\nAdjacency List after wrapping circuits")
    graph.PrintAdjacencyMap()

    # Count all nodes that have no incoming and are not the starting airport
    count = sum(1 for node in graph.nodemap.values() if graph.CountIncoming(node) == 0 and node.name != starting_airport)
    return count

def RunExample():
    airports = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]
    routes = [
        ("DSM", "ORD"), ("ORD", "BGI"), ("BGI", "LGA"), ("SIN", "CDG"), ("CDG", "SIN"), ("CDG", "BUD"),
        ("DEL", "DOH"), ("DEL", "CDG"), ("TLV", "DEL"), ("EWR", "HND"), ("HND", "ICN"), ("HND", "JFK"),
        ("ICN", "JFK"), ("JFK", "LGA"), ("EYW", "LHR"), ("LHR", "SFO"), ("SFO", "SAN"), ("SFO", "DSM"),
        ("SAN", "EYW")
    ]
    starting_airport = "LGA"
    answer = MinNewRoutes(airports, routes, starting_airport)

if __name__ == "__main__":
    RunExample()
