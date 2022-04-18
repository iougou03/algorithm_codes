import sys

input = sys.stdin.readline
print = sys.stdout.write
n = int(input())

arr = [0 for _ in range(10000)]

for _ in range(n): arr[int(input()) - 1] += 1

for i in range(10000):
    for _ in range(arr[i]):
        print(str(i + 1))