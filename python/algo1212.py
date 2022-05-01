oct = input()

ans = []
def oct2bin(oct_num):
    global ans
    for i in range(2, -1, -1):
        if oct_num >= 2**i:
            oct_num -= 2**i
            ans.append("1")
        else:
            ans.append("0")

for o in oct:
    oct2bin(int(o))

while len(ans) > 1 and ans[0] == "0":
    ans.pop(0)

print("".join(ans))
