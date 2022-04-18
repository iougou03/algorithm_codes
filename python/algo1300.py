n = int(input())

k = int(input())

left = 1 ; right = min(10**9, n**2)

def check_valid(num):
    global n, k
    cnt = 0

    for i in range(1, n + 1):
        if num // i > 0: cnt += min(num // i, n)
        else: break
    return cnt

while left < right:
    middle = (left + right) // 2
    val = check_valid(middle)
    
    if val < k: left = middle + 1
    else: right = middle

print(left)

# arr = [[i * j for j in range(1, n+1)] for i in range(1, n+1)]

# for a in arr:
#     [print(f"{c:3}", end=" ") for c in a]
#     print()

# '''

# S   1  2  3  4  5  6  7  8
# cnt 1  3  5  8  8 10 10 12

# '''