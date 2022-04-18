import sys
N, C = map(int, sys.stdin.readline().split())

house_address = []
for _ in range(N):
    house_address.append(int(sys.stdin.readline()))

house_address.sort()
# min_gap = house_address[1] - house_address[0]
min_gap = 1
max_gap = house_address[-1] - house_address[0]
ans = 0

def router_cnt(gap):
    prev_idx = 0 ; idx = 1 ; cnt = 1

    while(idx < N):
        if house_address[idx] - house_address[prev_idx] >= gap:
            cnt += 1 ; prev_idx = idx
        idx += 1

    return cnt 

while(min_gap < max_gap):
    middle = (max_gap + min_gap) // 2
    v = router_cnt(middle)

    if v < C: max_gap = middle - 1
    else : # v >= C
        min_gap = middle + 1 
        ans = min_gap

print(ans)

# 최대 gap을 "탐색"한다고 생각하면 쉽다.

# sort 
# 가설 : 정렬된 주소의 이분법적 left right에 설치하면 최대? -> 아님 (아래가 반례)
# 1 2 3 4 5 6 7 , (N,C) = (7,3)
# [1] 5 15 300 10000 [140000] [530002]