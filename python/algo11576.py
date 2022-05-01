import sys
input = sys.stdin.readline

A, B = map(int , input().split())
m = int(input())
aDigits = list(map(int, input().split()))
bDigits = []

decimalNum = 0
for i in range(m):
    exp = (m - i - 1)
    decimalNum += aDigits[i] * A ** exp

while decimalNum > 0:
    bDigits.append(decimalNum % B)
    decimalNum //= B

while bDigits: print(bDigits.pop(), end=" ")
