import sys
input = sys.stdin.readline

t = int(input())

def findRoot(person):
    if type(network[person]) != str:
        return person
    else:
        network[person] = findRoot(network[person])
        return network[person]

def unionNetwork(personA, personB):
    aRoot = findRoot(personA)
    bRoot = findRoot(personB)

    if aRoot != bRoot:
        network[aRoot] += network[bRoot]
        network[bRoot] = aRoot

    return network[aRoot]

def regist(person):
    if person not in network:
        network[person] = 1
for _ in range(t):
    n = int(input())
    network = {}

    for __ in range(n):
        a, b = input().split()
        regist(a) ; regist(b)

        print(unionNetwork(a, b))