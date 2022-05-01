# n = int(input())
# ans = 0
# for i in range(5, n + 1, 5):
#     while i % 5 == 0:
#         ans += 1
#         i //= 5

# print(ans)

n = int(input())
cnt2 = 0 ; cnt5 = 0

def count2div(num):
    global cnt2
    while num % 2 == 0:
        cnt2 += 1
        num //= 2
        
def count5div(num):
    global cnt5
    while num % 5 == 0:
        cnt5 += 1
        num //= 5

for i in range(1, n + 1): 
    count2div(i)
    count5div(i)

print(min(cnt2, cnt5))