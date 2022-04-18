import sys

N = int(sys.stdin.readline())
roads = []
cities = []

roads = list(map(int,(sys.stdin.readline().split()))) # length : N - 1
cities = list(map(int,(sys.stdin.readline().split()))) # length : N

def solution():
    idx = 0 ; price = 0

    for i in range(1, N):
        if cities[idx] > cities[i] or i == N - 1:
            for j in range(idx, i): 
                price += roads[j] * cities[idx]
            idx = i
    return price

print(solution())
