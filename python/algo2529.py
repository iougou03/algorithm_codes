k = int(input())
logic_seq = input().split()
visited = [0 for _ in range(10)]
maxNum = "0" ; minNum = "9876543211"

def solution(a, lidx, val):
    global k, maxNum, minNum
    if lidx == k:
        if int(maxNum) < int(val):
            maxNum = val
        if int(minNum) > int(val):
            minNum = val
        return

    for b in range(10):
        if a == b: continue

        if not visited[b] and eval(f'{a} {logic_seq[lidx]} {b}'):
            visited[b] = 1
            solution(b, lidx + 1, val + str(b))
            visited[b] = 0

for i in range(10):
    visited[i] = 1
    solution(i, 0, str(i))
    visited[i] = 0

print(maxNum)
print(minNum)