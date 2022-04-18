import sys, heapq

input = sys.stdin.readline

n = int(input())
coinTree = {
    "left": [],
    "middle": 0,
    "right": []
}

def getSize(): return len(coinTree["left"]) + 1 + len(coinTree["right"])
def addNumber(num):
    if num < coinTree["middle"]:
        heapq.heappush(coinTree["left"], [-num,num])
    else:
        heapq.heappush(coinTree["right"], num)
    
    if getSize() % 2 != 0:
        if len(coinTree["left"]) > len(coinTree["right"]):
            heapq.heappush(coinTree["right"], coinTree["middle"])
            coinTree["middle"] = heapq.heappop(coinTree["left"])  
        elif len(coinTree["left"]) < len(coinTree["right"]):
            heapq.heappush(coinTree["left"], [-coinTree["middle"], coinTree["middle"]])
            coinTree["middle"] = heapq.heappop(coinTree["right"])
    else:
        if len(coinTree["left"]) > len(coinTree["right"]):
            heapq.heappush(coinTree["right"], coinTree["middle"])
            coinTree["middle"] = heapq.heappop(coinTree["left"])[1]

num = int(input()) ; coinTree["middle"] = num ; ans = [num]

for i in range(n - 1):
    num = int(input())

    addNumber(num)
    ans.append(coinTree["middle"])    
    
[print(a) for a in ans]