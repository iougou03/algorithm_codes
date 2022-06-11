n = int(input()) # n <= 30
weight_seq = [0] + list(map(int, input().split())) # wi <= 500 ; sorted asc
t = int(input()) # t <= 7
test_seq = list(map(int, input().split())) # ti <= 40,000

dp = [[False] * (15001) for _ in range(n + 1)]
# we can put weight on the left side of the scale or 
# on the right side of the scale which does not 
# contain any marble, only weights
def solution(widx : int, weight_sum : int):

    if widx > n or dp[widx][weight_sum]: return

    dp[widx][weight_sum] = True

    solution(widx + 1, weight_sum + weight_seq[widx])
    solution(widx + 1, abs(weight_sum - weight_seq[widx]))
    solution(widx + 1, weight_sum)

solution(0, 0)

for i in range(t):
    if test_seq[i] > 15000: print("N", end=" ")
    elif dp[n][test_seq[i]]: print("Y", end=" ")
    else: print("N", end=" ")