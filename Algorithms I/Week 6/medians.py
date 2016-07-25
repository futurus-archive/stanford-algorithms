from collections import _heapq
f = open("Median.txt", 'r')
Hlow = [] # support extract Max
Hhigh = []# support extract Max
Medians = []

for line in f:
    e = int(line)
    if len(Hlow) > 0:
        if -e > Hlow[0]:
            _heapq.heappush(Hlow, -e)
        else:
            _heapq.heappush(Hhigh, e)
    else:
        _heapq.heappush(Hlow, -e)

    if len(Hlow) > len(Hhigh) + 1:
        f = _heapq.heappop(Hlow)
        _heapq.heappush(Hhigh, -f)
    elif len(Hhigh) > len(Hlow) + 1:
        f = _heapq.heappop(Hhigh)
        _heapq.heappush(Hlow, -f)

    if len(Hlow) > len(Hhigh) or len(Hlow) == len(Hhigh):
        Medians.append(-Hlow[0])
    elif len(Hhigh) > len(Hlow):
        Medians.append(Hhigh[0])

print(len(Medians))
print(sum(Medians))
print(sum(Medians) % 10000)