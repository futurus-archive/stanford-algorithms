f = open("2sum.txt", 'r')

hash = {}
answer = set()

for line in f:
    hash[int(line)] = 1

i = 0

for x in hash.keys():
    minPos = -10000 - x
    maxPos = +10000 - x

    for y in range(minPos, maxPos + 1):
        if y in hash and y != x:
            answer.add(x + y)

    if len(answer) == 20001:
        break

print(len(answer))
print(answer)