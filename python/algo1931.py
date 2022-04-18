# n = int(input())

# i_list = []
# # 1. 매시행마다 작은 회의시간을 가진 회의부터 소거
# # 2. 만약 이전것과 시간이 겹치면 제거
# def check_time(check_start, check_end, start, end):
#     if check_start == check_end:
#         if start < check_start and check_end < end: return False
#         elif start == check_start and end ==check_end: return False
#         else: return True
#     else:
#         if check_start < start < check_end or check_start < end < check_end: return False
#         elif start <= check_start and check_end <= end: return False
#         else: return True

# for _ in range(n):
#     start, end = map(int, input().split())
#     i_list.append((end - start, start, end))

# i_list = sorted(i_list, key= lambda x:x[0])
# check_tuples = [i_list[0]]
# ans = 1

# for i in range(1,n):
#     state = True
#     for ct in check_tuples:
#         if not check_time(ct[1], ct[2], i_list[i][1], i_list[i][2]):
#             state = False
#             break
#     if state: 
#         check_tuples.append(i_list[i])
#         ans+=1

# print(ans)

# version 2
import sys

N = int(sys.stdin.readline())
meetings = []

for _ in range(N):
    meetings.append(tuple(map(int, sys.stdin.readline().split())))

meetings = sorted(meetings)
meetings = sorted(meetings, key=lambda x: x[1])

ans = 1
end = meetings[0][1]
for i in range(1, N):
    if end <= meetings[i][0]:
        ans += 1
        end = meetings[i][1]

print(ans)