from time import time
import sys
sys.setrecursionlimit(100000)

# G = {7: [1], 5: [2], 9: [3, 7], 1: [4],
#      8: [5, 6], 2: [8], 6: [9], 3: [6], 4: [7]}
# Grev = {1: [7], 2: [5], 3: [9], 4: [1], 5: [8],
#      6: [3, 8], 7: [4, 9], 8: [2], 9: [6]}


start = time()
# read in data and set up
f = open('SCC.txt', 'r')
G = {}
Grev = {}

for line in f:
    head, tail = map(int, line.rstrip().split(' '))

    # populate G
    if head in G:
        G[head].append(tail)
    else:
        G[head] = [tail]

    # populate G reverse
    if tail in Grev:
        Grev[tail].append(head)
    else:
        Grev[tail] = [head]

print "Import finished"
end = time()
print end - start
start = end

# first pass
# performed on Grev
t = 0
f = {} # finishing time
frev = {}
explored = set([])

def dfs_loop1(Graph):
    for i in range(875714, 0, -1):
        if (i in Graph) and (i not in explored):
            dfs1(Graph, i)


def dfs1(Graph, i):
    global t
    explored.add(i)
    for j in Graph[i]:
        if (j in Graph) and (j not in explored):
            dfs1(Graph, j)

    t += 1
    f[i] = t
    frev[t] = i

print "1st pass init"
dfs_loop1(Grev)
print "1st pass finished"
end = time()
print end - start
start = end
# print f    # {1: 7, 2: 3, 3: 1, 4: 8, 5: 2, 6: 5, 7: 9, 8: 4, 9: 6}
# print frev # {1: 3, 2: 5, 3: 2, 4: 8, 5: 6, 6: 9, 7: 1, 8: 4, 9: 7}

# second pass
# perform on G, with nodes f(i) instead of i
scc = []
explored.clear()


def dfs_loop2(Graph):
    global scc
    for i in range(875714, 0, -1):
        if (i in Graph) and (i not in explored):
            s = dfs2(Graph, i)
            scc.append(s)


def dfs2(Graph, i):
    explored.add(i)
    # actual node
    # print frev[i]
    for j in Graph[frev[i]]:
        if (f[j] in Graph) and (f[j] not in explored):
            # dfs2(G, f[j])
            return [i] + dfs2(Graph, f[j])

    return [i]


print "2nd pass init"
dfs_loop2(G)
print "2nd pass finished"
end = time()
print end - start
start = end


scc = sorted(scc, key=lambda l: len(l), reverse=True)
lengths = [len(l) for l in scc]
print lengths