from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial, target):
    Q = set()
    prev = {}
    dist = {}

    for node in graph.nodes:
        prev[node] = None
        dist[node] = 1000000
        Q.add(node)

    dist[initial] = 0

    while len(Q) > 0:
        distQ = {}
        for e in Q:
            distQ[e] = dist[e]
        u = min(distQ, key=distQ.get)
        Q.remove(u)

        if u == target:
            return build_path(graph, prev, target)

        for v in graph.edges[u]:
            alt = dist[u] + graph.distances[(u, v)]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u


def build_path(graph, prev, target):
    seq = []
    u = target
    length = 0
    while prev[u] is not None:
        seq.append(u)
        length += graph.distances[(prev[u], u)]
        u = prev[u]
    seq.append(u)

    return seq, length


Nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]

G = Graph()
f = open("dijkstraData.txt", 'r')

for line in f:
    elems = line.split('\t')
    elems.pop(-1) # remove new line
    tail, heads = elems[0], elems[1:]

    for head in heads:
        h, length = head.split(',')
        G.add_node(int(tail))
        G.add_node(int(h))
        G.add_edge(int(tail), int(h), int(length))


for node in Nodes:
    seq, length = dijsktra(G, 1, node)
    print seq, length