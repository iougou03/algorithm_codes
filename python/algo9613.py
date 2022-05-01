from re import A


def get_gcd(a,b):
    if b > a: a,b = b,a

    while b > 0:
        temp = a % b
        a = b
        b = temp
    
    return a

t = int(input())

for _ in range(t):
    numList = list(map(int , input().split()))
    ans = 0
    for i in range(1, numList[0]):
        for j in range(i + 1, numList[0] + 1):
            ans +=get_gcd(numList[i], numList[j])

    print(ans)
    