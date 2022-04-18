import sys

input = sys.stdin.readline
k, n = map(int, input().split())
lans_list = []

for _ in range(k): 
    val = int(input())
    lans_list.append(val)

lans_list.sort(reverse=True)
left = 0 ; right = lans_list[0]

def check_valid(lan, needs):
    cnt = 0
    for l in lans_list:
        if cnt >= needs: return True
        val = l
        while val - lan >= 0:
            cnt += 1
            val -= lan
    
    if cnt < needs: return False
    else: return True

while left < right:
    middle = (left + right) // 2
    
    if check_valid(middle, n): left = middle + 1
    else: right = middle 

print(right - 1)