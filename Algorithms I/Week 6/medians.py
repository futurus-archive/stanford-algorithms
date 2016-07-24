from collections import _heapq

f = open("Median.txt", 'r')

Hlow = [] # support extract Max
Hhigh = []# support extract Max
Medians = []

for line in f:
    e = int(line)
    if len(Hlow) == len(Hhigh):
        _heapq.heappush(Hlow, -e)
        Medians.append(e)
    else:
        if -e > Hlow[0]:
            if len(Hlow) > len(Hhigh):
                f = _heapq.heappushpop(Hlow, -e)
                _heapq.heappush(Hhigh, -f)
                Medians.append(-Hlow[0])
            else:
                _heapq.heappush(Hlow, -e)
                Medians.append(Hhigh[0])
        elif e > Hhigh[0]:
            if len(Hhigh) > len(Hlow):
                f = _heapq.heappushpop(Hhigh, e)
                _heapq.heappush(Hlow, -f)
                Medians.append(Hhigh[0])
            else:
                _heapq.heappush(Hhigh, e)
                Medians.append(-Hlow[0])

    # print("i: ", i)
    # print("element: ", e)
    # print("Hlow: ", Hlow)
    # print("Hhigh: ", Hhigh)
    # print("Medians: ", Medians)

print(Medians)
print(sum(Medians))
print(sum(Medians) % 10000)