f = open("2sum.txt", 'r')

hash = {}
answer = set()

for line in f:
    hash[int(line)] = 1

for t in range(-10000, 10001):
    for x in hash.keys():
        y = t-x
        if y is not x and y in hash:
            answer.add(t)
            break

print(len(answer))
print(answer)