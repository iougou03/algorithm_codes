n = int(input())
weight = list(map(int , input().split()))
ans = 0

def solution(arr, val):
    global ans

    if len(arr) == 2:
        ans = max(ans, val)
        return
    
    for i in range(1, len(arr) - 1):
        solution(arr[:i] + arr[i + 1:], val + arr[i - 1] * arr[i + 1])

solution(weight, 0)

print(ans)
        