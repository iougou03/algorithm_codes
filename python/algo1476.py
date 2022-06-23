E, S, M = map(int, input().split())

earth = 0 ; sun = 0 ; moon = 0
year = 0

while not (earth == E and sun == S and moon == M):
    year += 1

    earth = earth + 1 if earth + 1 <= 15 else 1
    sun = sun + 1 if sun + 1 <= 28 else 1
    moon = moon + 1 if moon + 1 <= 19 else 1

print(year)