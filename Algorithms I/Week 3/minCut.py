from random import randrange, shuffle, choice
import copy


class Vertex:
    def __init__(self, v):
        self.v = set([v])

    def add(self, vertex):
        # for vertex contraction
        self.v = self.v.union(vertex.prtV())

    def prtV(self):
        return self.v

    def num(self):
        return len(self.v)

    def equals(self, other):
        if self.v.intersection(other.v) == self.v:
            return True
        else:
            return False

    def contains(self, other):
        return self.v.issuperset(other.v)


class Edge:
    def __init__(self, src, des):
        self.src = src
        self.des = des

    def src(self):
        return self.src

    def des(self):
        return self.des

    def contractSrc(self, v):
        self.src.add(v)

    def contractDes(self, v):
        self.des.add(v)

    def prtE(self):
        print self.src.prtV()
        print " -- "
        print self.des.prtV()


class Graph:
    def __init__(self, input):
        self.edges = set([])
        self.vertices = set([])

        f = open(input, 'r')

        for line in f:
            elems = line.split('\t')
            elems.pop(-1)
            nodes = map(int, elems)
            src = Vertex(nodes[0])
            self.vertices.add(src)

            for node in nodes[1:]:
                des = Vertex(node)
                self.edges.add(Edge(src, des))

        self.edges = list(self.edges)
        self.nvertices = len(self.vertices)
        self.nedges = len(self.edges)


g = Graph("_kargerMinCut.txt")
i = 0
vertices = copy.deepcopy(g.vertices)
edges = copy.deepcopy(g.edges)

while len(vertices) > 100:
    i += 1
    # pick a random edge
    e = choice(g.edges)
    v1 = copy.deepcopy(e.src)
    v2 = copy.deepcopy(e.des)

    if not v1.equals(v2):
        print i, ": contracting ", v1.prtV(), " and ", v2.prtV()

        # take care of edges
        for edge in g.edges:
            if edge.src.equals(v1) and edge.des.equals(v2):
                # skip the exact same edge
                continue

            if edge.src.equals(v1):
                # modify all edges so that the src now includes v2
                edge.src.add(v2)

            if edge.des.equals(v2):
                # modify all edges so that the des now includes v1
                edge.des.add(v1)

        # edge e is contracted, remove it from graph g
        g.edges.remove(e)

        # combine vertices
        for v in vertices:
            if v.equals(v1):
                print repr(v.prtV()) + " vs. " + repr(v1.prtV())
                v.add(v2)
                print repr(v.prtV())
                break

        for v in vertices:
            if v.equals(v2):
                vertices.discard(v)
                break


vertices = list(vertices)
sum = 0
for v in vertices:
    sum += v.num()
print sum

print vertices[0].prtV()
print len(vertices[0].prtV())
print vertices[1].prtV()
print len(vertices[1].prtV())
